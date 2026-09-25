#!/usr/bin/env python3
"""Avisa a los buscadores que soportan IndexNow (Bing, Yandex, Seznam, Naver)
que estas URL cambiaron. Se ejecuta a mano después de un despliegue:

    python3 indexnow.py

La clave vive en f42d097b2239e1408b611e91d388c718.txt, en la raíz del sitio, que es como IndexNow
comprueba que quien avisa es el dueño del dominio.
"""
import json
import urllib.request

CLAVE = "f42d097b2239e1408b611e91d388c718"
HOST = "az900.sintitulo.dev"
URLS = [
    f"https://{HOST}/",
    f"https://{HOST}/practica",
    f"https://{HOST}/diferencias",
    f"https://{HOST}/metodo",
    f"https://{HOST}/examen",
]

cuerpo = json.dumps({
    "host": HOST,
    "key": CLAVE,
    "keyLocation": f"https://{HOST}/{CLAVE}.txt",
    "urlList": URLS,
}).encode()

peticion = urllib.request.Request(
    "https://api.indexnow.org/IndexNow",
    data=cuerpo,
    headers={"Content-Type": "application/json; charset=utf-8"},
)

with urllib.request.urlopen(peticion) as respuesta:
    print(respuesta.status, respuesta.reason)
