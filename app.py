import streamlit as st
import qrcode
from PIL import Image, ImageDraw
import io

# Define uma função para colocar o QR Code na imagem
def put_qr_code(image, qr_code, x, y):
    qr_width, qr_height = qr_code.size
    image_width, image_height = image.size
    x -= qr_width / 2
    y -= qr_height / 2
    if x < 0:
        x = 0
    elif x + qr_width > image_width:
        x = image_width - qr_width
    if y < 0:
        y = 0
    elif y + qr_height > image_height:
        y = image_height - qr_height
    image.paste(qr_code, (int(x), int(y)))

# Define a função principal do aplicativo
def main():
    # st.image('https://static.springbuilder.site/fs/userFiles-v2/bet77-18750706/images/logo.png?v=1664188629', width=200)
    st.image('https://wmmtech.com.br/img/logo-wmm.png', width=200)
    st.title("Gerador de QR CODE com Imagem")

    # Carrega a imagem e o texto do QR Code
    image_file = st.file_uploader("Selecione uma imagem", type=["jpg", "jpeg", "png"])
    qr_text = st.text_input("Digite o link para o QR Code")

    # Define as resoluções disponíveis
    resolutions = {
        "Post Instagram": (1080, 1080),
        "Story Instagram": (1080, 1932)
    }

    # Pede ao usuário para selecionar a resolução desejada
    resolution = st.selectbox("Selecione a resolução da imagem", list(resolutions.keys()))

    # Verifica se o arquivo de imagem e o texto foram fornecidos
    if image_file is not None and qr_text:
        # Carrega a imagem e gera o QR Code
        image = Image.open(image_file)
        qr_code = qrcode.make(qr_text)

        # Pede ao usuário para especificar a posição do QR Code
        x = st.slider("Posição X", 0, image.width, step=1)
        y = st.slider("Posição Y", 0, image.height, step=1)

        # Coloca o QR Code na imagem
        put_qr_code(image, qr_code, x, y)

        # Redimensiona a imagem para a resolução selecionada
        image = image.resize(resolutions[resolution])

        # Exibe o resultado
        st.image(image, caption="Imagem com QR Code e resolução {}".format(resolution))

                # Adiciona um botão de download para a imagem gerada
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='PNG')
        st.download_button(
            label="Baixar Imagem",
            data=img_bytes.getvalue(),
            file_name="qr_code.png",
            mime="image/png"
        )

# Executa a função principal
if __name__ == "__main__":
    main()