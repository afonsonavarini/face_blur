# face_blur
## Alunos: Afonso Navarini e Bruno Fraga Benetti

## Descrição
Algoritmo aplica BLUR na face detectada para garantir privacidade. Ao apontar um objeto de cor vermelha, é ativado um Easter Egg de Modo Palhaço, registrando a data do evento. Ao apontar a cor verde, o algoritmo volta ao normal.

## Libs Utilizadas
- OpenCV2
- Numpy
- Datetime (nativo)

## Funcionamento
Imagem 1: Algoritmo carrega o haarcascade de detecção facial, detecta a face e aplica o blur na área detectada.

![Imagem_1](https://user-images.githubusercontent.com/63884763/203121853-0c6075d7-2651-4b81-a60f-abeca27dd796.png)

Imagem 2: Ao apontar uma cor vermelha à camera, o haarcascade muda para detecção nasal, aplicando um círculo na área que se ajusta de acordo com a distância.

![Imagem_2](https://user-images.githubusercontent.com/63884763/203122175-bfcbc46d-1b96-4287-b630-28f0af493466.png)

Imagem 3: A aplicação volta ao normal ao apontar uma cor verde à camera.

![Imagem_3](https://user-images.githubusercontent.com/63884763/203122288-0f76dde9-f004-4fed-9998-76b3c888314f.png)

Imagem 4: Log gerado registrando a data e hora do evento em que o "Modo Palhaço" foi ativo.

![Imagem_4](https://user-images.githubusercontent.com/63884763/203122378-a0c5cccd-e7f2-4aa4-bf48-00390d9d6f6f.png)
