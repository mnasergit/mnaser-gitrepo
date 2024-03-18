import base64

encoded_value = "CiEKISBMYXN0IGNvbmZpZ3VyYXRpb24gY2hhbmdlIGF0IDAwOjA0OjM4IFVUQyBXZWQgSmFuIDE3IDIwMjQgYnkgYXBuaWMKIQp2ZXJzaW9uIDE1LjIKc2VydmljZSB0aW1lc3RhbXBzIGRlYnVnIGRhdGV0aW1lIG1zZWMKc2VydmljZSB0aW1lc3RhbXBzIGxvZyBkYXRldGltZSBtc2VjCnNlcnZpY2UgcGFzc3dvcmQtZW5jcnlwdGlvbgohCmhvc3RuYW1lIEdyb3VwMS1Sb3V0ZXIxCiEKYm9vdC1zdGFydC1tYXJrZXIKYm9vdC1lbmQtbWFya2VyCiEKIQohCm5vIGFhYSBuZXctbW9kZWwKIQohCiEKIQohCiEKbm8gaXAgZG9tYWluIGxvb2t1cAppcCBkb21haW4gbmFtZSBhcG5pYy5uZXQKaXAgY2VmCm5vIGlwdjYgY2VmCiEKIQptdWx0aWxpbmsgYnVuZGxlLW5hbWUgYXV0aGVudGljYXRlZAohCiEKIQohCiEKIQohCnVzZXJuYW1lIGFwbmljIHByaXZpbGVnZSAxNSBzZWNyZXQgNSAkMSRZTDUxJGJJSzVvV1B4Sm1yRDduaHZ6WVZRRzAKIQohCiEKIQohCmlwIHNzaCB2ZXJzaW9uIDIKISAKIQohCiEKIQohCiEKIQohCmludGVyZmFjZSBGYXN0RXRoZXJuZXQwLzAKIG5vIGlwIGFkZHJlc3MKIHNodXRkb3duCiBkdXBsZXggZnVsbAohCmludGVyZmFjZSBGYXN0RXRoZXJuZXQxLzAKIG5vIGlwIGFkZHJlc3MKIHNodXRkb3duCiBkdXBsZXggZnVsbAohCmludGVyZmFjZSBGYXN0RXRoZXJuZXQyLzAKIG5vIGlwIGFkZHJlc3MKIHNodXRkb3duCiBkdXBsZXggZnVsbAohCmludGVyZmFjZSBGYXN0RXRoZXJuZXQzLzAKIG5vIGlwIGFkZHJlc3MKIHNodXRkb3duCiBkdXBsZXggZnVsbAohCmludGVyZmFjZSBGYXN0RXRoZXJuZXQ0LzAKIG5vIGlwIGFkZHJlc3MKIHNodXRkb3duCiBkdXBsZXggZnVsbAohCmludGVyZmFjZSBGYXN0RXRoZXJuZXQ1LzAKIG5vIGlwIGFkZHJlc3MKIHNodXRkb3duCiBkdXBsZXggZnVsbAohCmludGVyZmFjZSBGYXN0RXRoZXJuZXQ2LzAKIGRlc2NyaXB0aW9uICoqTUdNVCAtIERvIE5vdCBEZWxldGUqKgogaXAgYWRkcmVzcyAxMC45OS4xLjEgMjU1LjI1NS4wLjAKIGR1cGxleCBmdWxsCiBpcHY2IGFkZHJlc3MgMjQwNjo2NDAwOjk5OjoxOjEvNjQKIQppcCBmb3J3YXJkLXByb3RvY29sIG5kCiEKIQpubyBpcCBodHRwIHNlcnZlcgpubyBpcCBodHRwIHNlY3VyZS1zZXJ2ZXIKIQohCiEKIQpjb250cm9sLXBsYW5lCiEKIQpsaW5lIGNvbiAwCiBleGVjLXRpbWVvdXQgMCAwCiBsb2dnaW5nIHN5bmNocm9ub3VzCmxpbmUgYXV4IDAKbGluZSB2dHkgMCA0CiBleGVjLXRpbWVvdXQgMCAwCiBsb2dnaW5nIHN5bmNocm9ub3VzCiBsb2dpbiBsb2NhbAogdHJhbnNwb3J0IGlucHV0IGFsbAohCmV2ZW50IG1hbmFnZXIgYXBwbGV0IHdyaXRlX21lbSBhdXRob3JpemF0aW9uIGJ5cGFzcwogZXZlbnQgdGltZXIgY291bnRkb3duIHRpbWUgODAKIGFjdGlvbiAxLjAgY2xpIGNvbW1hbmQgImVuYWJsZSIKIGFjdGlvbiAxLjEgY2xpIGNvbW1hbmQgIndyaXRlIG1lbSIKZXZlbnQgbWFuYWdlciBhcHBsZXQgY3J5cHRvX2tleSBhdXRob3JpemF0aW9uIGJ5cGFzcwogZXZlbnQgdGltZXIgY3JvbiBjcm9uLWVudHJ5ICJAcmVib290IiBtYXhydW4gNjAKIGFjdGlvbiAxLjAgY2xpIGNvbW1hbmQgImVuYWJsZSIKIGFjdGlvbiAxLjEgY2xpIGNvbW1hbmQgImNvbmZpZyB0IgogYWN0aW9uIDEuMiBjbGkgY29tbWFuZCAiY3J5cHRvIGtleSBnZW5lcmF0ZSByc2EgbW9kdWx1cyAxMDI0IgogYWN0aW9uIDEuMyBjbGkgY29tbWFuZCAiZW5kIgogYWN0aW9uIDEuNCBjbGkgY29tbWFuZCAid3JpdGUgbWVtIiBwYXR0ZXJuICJjb25maXJtfCMiCiBhY3Rpb24gMS41IHJlZ2V4cCAiY29uZmlybSIgIiRfY2xpX3Jlc3VsdCIKIGFjdGlvbiAxLjYgaWYgJF9yZWdleHBfcmVzdWx0IGVxICIxIgogYWN0aW9uIDEuNyAgY2xpIGNvbW1hbmQgInkiCiBhY3Rpb24gMS44IGVuZAogYWN0aW9uIDEuOSBjbGkgY29tbWFuZCAiY29uZmlnIHQiCiBhY3Rpb24gMi4wIGNsaSBjb21tYW5kICJubyBldmVudCBtYW5hZ2VyIGFwcGxldCBjcnlwdG9fa2V5IgohCmVuZAo="
decoded_value = base64.b64decode(encoded_value).decode('utf-8')
print(decoded_value)
