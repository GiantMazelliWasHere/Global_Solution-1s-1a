# GS-Edge_Computing

- Eduardo Mazelli - 553236
- Nathan da Silveira Uflacker - 553264

Link Thinkercad:
https://www.tinkercad.com/things/kmAqoo2wNC6-gs-edge-computing/editel

Link Video YouTube:
https://www.youtube.com/watch?v=9W4W4TpeRwc

Descrição do Problema:

Muitas vezes vamos em pronto socorros e hospitais e por falta de uma pré triagem pegamos uma fila enorme e ficamos esperando por muito tempo. Quando estamos apenas com um estado febril essa espera é algo suportável e que não fará muita diferença, mas quando estamos com uma febre de 38, ou até uma febre alta de 39/40 graus essa espera, não só se torna insuportável como podemos sofrer de alguns sintomas extras se esperarmos demais.

Visão Geral da Solução:

Por isso desenvolvemos esse dispositivo que quando o paciente entra no pronto socorro ou hospital, ela irá medir a temperatura dele e assim baseado nessa pré triagem, definirá qual fila ele deve pegar entre: 
- Baixo risco: Pessoas com 36,9 ou menos de febre;
- Risco Médio: Pessoas entre 37 e 38,9 de febre;
- Alto risco: Pessoal com 39 ou mais de Febre.
Assim direcionando elas para diferentes filas com um referencial diferente. 

Como Montar:

Você precisará:
1 Arduino Uno;
1 Protoboard Grande;
1 Resistor de 220Ω;
1 Potenciômetro;
1 LCD de 16x2;
1 Sensor ultrasônico;
1 Sensor de temperatura.

Na Protoboard:
 Conecte as saídas positivas da protoboard na entrada 5v, e a negativa no gnd do arduino. Conecte as saídas positiva e negativa do lado oposto da protoboard no lado conectado ao arduino. 

Sensor Ultrasônico:
 Conecte a entrada vcc numa das saídas positivas da protoboard. Conecte as entradas ‘trig’ e ‘echo’ direto no arduino, e forneça os números das portas conectadas para o código. Conecte a entrada gnd numa saída negativa da protoboard.

Sensor de temperatura:
 Conecte a perna do lado esquerdo numa das saídas positivas da protoboard e a perna esquerda na saída negativa. A perna do meio conecte numa das portas com o nome de Analog do Arduino e forneça o número para o código, no seu padrão ‘A(número da porta)’

Potenciômetro:
 Conecte a perna esquerda numa saída positiva da protoboard e a perna direita numa negativa. A perna do meio será conectada com o LCD.

Resistor:
 Conecte uma perna numa saída positiva da protoboard e a outra dentro da protoboard. Conectarmos essa perna com o LCD.

LCD:
 Conecte a entrada gnd com uma saída negativa da protoboard e a vcc com uma saída positiva. A entrada ‘VO’ conecta-se com a perna do meio do potenciômetro. A entrada ‘RS’ conecta-se direto no arduino, a entrada ‘RW’ conecta-se com uma saída negativa da protoboard. As entradas ‘E’, ‘DB4’, ‘DB5’, ‘DB6’, ‘DB7’ conectamos diretamente no arduino. A primeira porta LED conectamos com o resistor e a segunda conectamos com uma saída negativa da protoboard. No código devemos passar todas as portas que usamos do arduino em ordem decrescente, ou seja da porta usada no RS até a porta usada no DB7.
