<h1 align="center"> Checkpoint 2 - Análise de Vogais em Libras com Arduino </h1>
<div> 
<h3> Integrantes do grupo: </h3> 
  <ul> 
    <li> Guilherme Doretto Sobreiro      | RM:99674 </li>
    <li> Guilherme Fazito Ziolli Sordini | RM:99674 </li>
    <li> Raí Gumieri dos Santos          | RM:99674 </li>
  </ul>
</div>

<div> 
<h2 align="center"> Ideia do Projeto </h2>
<p align="justify"> A proposta deste projeto é desenvolver um programa capaz de reconhecer as vogais em Libras (Língua Brasileira de Sinais), permitindo que o usuário utilize um vídeo gravado ou a webcam para capturar os gestos com as mãos. Quando o usuário realiza uma vogal em Libras, o programa exibe, em tempo real, a letra correspondente na tela. Além disso, para integrar o projeto ao Arduino, foi utilizado um display LCD I2C, possibilitando a visualização das vogais diretamente no dispositivo. </p>
</div>

<h2 align="center"> Equipamentos Necessários </h2>
<ul> 
  <li> Arduino UNO </li>
  <li> 4 Cabos Jumper (preferencialmente macho-fêmea) </li>
  <li> Display LCD I2C </li>
  <li> Cabo USB (para conexão com o Arduino) </li>
  <li> Webcam (caso opte por capturar os gestos em tempo real) </li>
</ul>

<h2 align="center"> Processo de Desenvolvimento </h2>

<h2> Código em Python </h2>
<p align="justify"> Antes de iniciar o desenvolvimento do código em Python, é necessário instalar o Anaconda, uma distribuição que facilita a gestão de pacotes e ambientes para ciência de dados. </p>
<h5> Link de instalação: https://www.anaconda.com/download </h5>
<p align="justify"> O Anaconda fornece todas as bibliotecas essenciais para o projeto, como o OpenCV, MediaPipe e outras ferramentas necessárias para a detecção de gestos em tempo real. </p>

<p align="center"> Após essa etapa, selecione o CMD.exe: </p>

<div align="center"> 
  <img src="https://github.com/user-attachments/assets/0c21f328-4470-41ad-ba6a-aa8c95f99006">
</div>

<br> 

<p align="center"> Digite o comando: </p>
<p align="center"> pip install matplotlib opencv-python notebook pyserial mediapipe   </p>

<div align="center"> 
  <img src="https://github.com/user-attachments/assets/fda0ad57-12ba-4c67-80e3-64a411fd802f">
</div>

<br>

<p align="center"> Após concluir a instalação das bibliotecas, abra o Visual Studio Code pelo Anaconda: </p>
<div align="center"> 
  <img src="https://github.com/user-attachments/assets/2eaf63b1-e8a6-4b5d-8453-d869e05ff440">
</div>

<p> Lembre-se de alterar a porta em que o Arduino está conectado. No código, a porta está definida como "COM5", mas ela pode variar de acordo com a porta USB utilizada no seu computador. </p>

<hr>

<h2> Código do Arduino </h2>
<p> Para programar o código no Arduino, será necessário instalar a IDE oficial. </p>
<h5> Link para instalar o Arduino IDE: https://www.arduino.cc/en/software/ </h5>

<p align="justify"> Após abrir a Arduino IDE, instale a biblioteca correspondente ao Display LCD I2C. Essa biblioteca é essencial para garantir o funcionamento correto da exibição das vogais no display.</p>

<div align="center">
  <img src="https://github.com/user-attachments/assets/5b655129-6065-4726-85cb-b2d6f5d5c488">
</div>

<p align="justify"> É importante definir a porta à qual o Arduino está conectado. Para isso, selecione as opções: Tools -> Board -> Arduino AVR Boards -> Arduino Uno. </p>
<p align="justify"> Em seguida, verifique se a porta correta está selecionada em Tools -> Port, garantindo que o Arduino esteja devidamente configurado para a comunicação com o código. </p>

<div align="center">
  <img src="https://github.com/user-attachments/assets/d0bd5b4c-a641-42f2-a094-31bdfbae5033">
</div>

<hr>

<h2> Etapa Final </h2>
<p align="justify"> Agora que você completou todas as etapas para preparar o ambiente, basta rodar ambos os códigos e testar com um vídeo ou a webcam. Coloque sua mão no centro da tela e inicie os gestos em Libras. Na parte superior, o programa exibirá a letra que está sendo analisada, e essa informação também será enviada para o display LCD. </p>

<div style="display: flex; justify-content: space-between;">
    <img src="https://github.com/user-attachments/assets/a39c9cfb-2bce-4f77-bb8d-fccb36b8efb1" width="45%">
    <img src="https://github.com/user-attachments/assets/5a7a5c54-a2ac-43f3-bbea-f84e21366abb" width="45%">
</div>

<p align="justify"> Durante os testes realizados por um integrante do grupo, Guilherme Doretto Sobreiro, o programa foi capaz de identificar em tempo real o sinal em Libras feito pela pessoa. O gesto foi reconhecido e, automaticamente, o programa exibiu a vogal correspondente no canto superior esquerdo da tela, além de enviar a informação para o display LCD, indicando a vogal que estava sendo transmitida ao Arduino. </p>

<hr>

<h2 align="center"> Dificuldades Encontradas </h2>
<p align="justify"> Durante a realização da atividade, encontramos algumas dificuldades ao tentar utilizar programas que faziam a comunicação com o Arduino e as portas virtuais. No entanto, conseguimos avançar com o uso do Arduino físico. Além disso, enfrentamos problemas ao carregar o vídeo e a webcam, que estavam travando devido à tentativa de conexão com o Arduino. Quando o programa não conseguiu se conectar inicialmente, isso afetou o desempenho do vídeo e da webcam. Contudo, após identificar a causa, conseguimos solucionar todos os problemas e o projeto está funcionando normalmente. </p>

<hr>

<h2 align="center"> Considerações Finais </h2>
<p align="justify"> O projeto foi concluído com sucesso, permitindo a identificação das vogais em Libras em tempo real, tanto com vídeos gravados quanto com a webcam. Superamos alguns desafios, como problemas de conexão e travamentos, mas conseguimos solucioná-los e garantir o funcionamento do sistema. A integração com o Arduino e o display LCD I2C foi eficiente para exibir as vogais detectadas. Este projeto demonstrou como é possível combinar software e hardware para criar soluções interativas e inclusivas, promovendo a comunicação por Libras de forma simples e acessível. </p>
