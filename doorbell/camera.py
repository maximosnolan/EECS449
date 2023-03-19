import cv2
import socket


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("localhost", 9925))
        sock.listen()

        # Block for a max of 1 second
        sock.settimeout(1)

        while True:
            try:
                clientsocket, address = sock.accept()
            except socket.timeout:
                continue

            clientsocket.settimeout(1)

            with clientsocket:
                try:
                    data = clientsocket.recv(1)
                except socket.timeout:
                    continue

                if data == b'E':
                    print(f'Image request from: {address[0]}:{address[1]}')
                    image = capture_image()
                    if not image:
                        image = 'No image was captured from the camera.'
                        print(image)
                        clientsocket.sendall(image.encode('utf-8'))
                    else:
                        image, h, w = image
                        image += b'-' + h.to_bytes(4, 'little') + b'-' + w.to_bytes(4, 'little')
                        clientsocket.sendall(image)


def capture_image():
    """
    Captures an image on the computer's camera
    :return: The encoded image from the camera, or an empty string
             if no image was captured
    """
    # TODO this device # is messed up
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)

    result, image = cam.read()
    print(image)
    return (image.flatten().tobytes(), image.shape[0], image.shape[1]) if result else None


if __name__ == "__main__":
    main()