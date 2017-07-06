<h1>Espelhamento de Tela *<i>Não nomeado ainda</i></h1>


<ol>

  <li type='disc'>
    Descrição:
    <ul>
      <li>
        Desenvolvido em python, este projeto tem como objetivo possibilitar o acesso remoto entre computadores e <b>futuramente</b> entre plataformas diferentes.
      </li>
       </br>
      <li>
        Para alcaçar os objetos, atualmente usa-se o protocolo TCP (<i>passível de mudança para UDP</i>) e utiliza de algumas bibliotecas <i>extras</i> para atingir o atual objetivo.</br>
        Algumas dessas bibliotecas são: </br>
        <i>pillow</i> - Utilizado para manipulação de imagens.</br>
        <i>pyautogui</i> - Utilizado para manipulação do ponteiro do mouse e captura de tela.
      </li>
      </br>
      <li>
        O transporte é feito da seguinte forma:</br>
        Qualquer pacote a ser enviado, é prefixado com alguns bytes a mais:</br>
          ><i>Tamanho</i>: os primeiros 4 bytes</br>
          >>Os primeiros quatro bytes definem o tamanho do pacote para que se ajuste o tamanho do buffer dinamicamente de acordo com a necessidade.</br>
          ><i>Tipo de pacote</i>: os próximos 4 bytes</br>
          >>Os próximos 4 bytes definem qual o tipo de pacote, se é imagem ou coordenadas do mouse, etc.
      </li>
    </ul>
  </li>
  
</ol>
