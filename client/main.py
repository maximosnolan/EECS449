import argparse
import socket
import numpy as np
import cv2

def main():
    request_image()


def request_image():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('localhost', 9925))
        sock.sendall('E'.encode('utf-8'))

        sock.settimeout(1)

        message_chunks = []
        while True:
            try:
                data = sock.recv(1024)
            except socket.timeout:
                continue
            if not data:
                break
            message_chunks.append(data)

        encoded_im = b''.join(message_chunks)
        image, height, width = encoded_im.split(b'-')  # split by null terminator
        height = int.from_bytes(height, 'little')
        width = int.from_bytes(width, 'little')
        image = np.frombuffer(image, dtype=np.uint8).reshape((height, width, 3))
        # print(image)
        # cv2.imshow('boingus', image)
        # cv2.waitKey(0)

if __name__ == "__main__":
    main()