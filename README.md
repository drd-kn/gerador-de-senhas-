# gerador-de-senhas-
gerador de senhas aleatorias

🔐 Gerador de Senhas Aleatórias | Random Password Generator

Idiomas / Languages: 🇧🇷 Português · 🇺🇸 English

🇧🇷 Português (PT-BR)
Visão geral

Script em Python que gera uma senha aleatória de 15 caracteres, combinando letras maiúsculas e minúsculas, dígitos e símbolos de pontuação. Utiliza apenas a biblioteca padrão da linguagem (random e string), sem dependências externas.

Código
python
import random, string

caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choices(caracteres, k=15))
print(f'Sua nova senha é: {senha}')
Como funciona
Importação dos módulos: random fornece a amostragem aleatória e string fornece constantes prontas com conjuntos de caracteres.
Construção do alfabeto: string.ascii_letters (52 letras) + string.digits (10 dígitos) + string.punctuation (32 símbolos) formam um conjunto de 94 caracteres.
Sorteio: random.choices(caracteres, k=15) sorteia 15 caracteres com reposição, ou seja, o mesmo caractere pode aparecer mais de uma vez.
Montagem: ''.join(...) concatena a lista sorteada em uma única string.
Saída: print exibe a senha gerada no terminal.

Espaço de possibilidades: 94¹⁵ ≈ 4,6 × 10²⁹ combinações (cerca de 98 bits de entropia), o que torna ataques de força bruta inviáveis para uma senha gerada dessa forma.

Requisitos
Python 3.6 ou superior (random.choices foi introduzido na versão 3.6)
Nenhuma biblioteca externa
Como executar
bash
python gerador_senhas.py

Exemplo de saída:

Sua nova senha é: k#9Zp!vR2@wLq8T
Situação hipotética

Uma startup de tecnologia contrata 50 novos colaboradores em um mês, e o time de TI precisa criar contas com credenciais temporárias para cada um. Se as senhas forem definidas manualmente, tendem a seguir padrões previsíveis (por exemplo, Empresa@123), o que as torna vulneráveis a ataques de dicionário e de preenchimento de credenciais.

Com este script, o time gera uma senha imprevisível, de alta entropia, para cada conta em segundos. Isso elimina o viés humano na escolha da senha, padroniza o processo e reduz o risco de acessos indevidos durante o período em que a senha temporária ainda não foi trocada.

Limitações e possíveis melhorias
Segurança criptográfica: o módulo random usa um gerador pseudoaleatório (Mersenne Twister), adequado para fins didáticos, mas não recomendado para uso em produção. Para senhas reais, o ideal é substituir por secrets.choice, que usa uma fonte criptograficamente segura.
Comprimento fixo: o tamanho (15) está definido no código; pode ser parametrizado via argumento de linha de comando ou função.
Composição não garantida: como o sorteio é uniforme sobre todo o alfabeto, não há garantia de que a senha contenha ao menos um caractere de cada categoria (maiúscula, minúscula, dígito, símbolo).
Evolução natural: encapsular a lógica em uma função reutilizável, adicionar testes unitários e uma interface de linha de comando (argparse).
🇺🇸 English
Overview

A Python script that generates a random 15-character password by combining uppercase and lowercase letters, digits, and punctuation symbols. It relies only on the standard library (random and string), with no external dependencies.

Code
python
import random, string

caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choices(caracteres, k=15))
print(f'Sua nova senha é: {senha}')
How it works
Module imports: random provides random sampling, and string provides ready-made character set constants.
Building the alphabet: string.ascii_letters (52 letters) + string.digits (10 digits) + string.punctuation (32 symbols) form a pool of 94 characters.
Sampling: random.choices(caracteres, k=15) draws 15 characters with replacement, meaning the same character may appear more than once.
Assembly: ''.join(...) concatenates the sampled list into a single string.
Output: print displays the generated password in the terminal.

Search space: 94¹⁵ ≈ 4.6 × 10²⁹ combinations (about 98 bits of entropy), which makes brute-force attacks infeasible against a password generated this way.

Requirements
Python 3.6 or higher (random.choices was introduced in 3.6)
No external libraries
Usage
bash
python gerador_senhas.py

Sample output:

Sua nova senha é: k#9Zp!vR2@wLq8T
Hypothetical scenario

A tech startup hires 50 new employees in a single month, and the IT team must create accounts with temporary credentials for each one. When passwords are chosen manually, they tend to follow predictable patterns (e.g., Company@123), making them vulnerable to dictionary attacks and credential stuffing.

With this script, the team can generate an unpredictable, high-entropy password for each account in seconds. This removes human bias from password selection, standardizes the process, and reduces the risk of unauthorized access during the window in which the temporary password has not yet been changed.

Limitations and possible improvements
Cryptographic security: the random module uses a pseudo-random generator (Mersenne Twister), which is fine for learning purposes but not recommended for production use. For real passwords, it should be replaced with secrets.choice, which draws from a cryptographically secure source.
Fixed length: the length (15) is hardcoded; it could be parameterized through a command-line argument or a function parameter.
Composition not guaranteed: since sampling is uniform over the whole alphabet, the password is not guaranteed to contain at least one character from each category (uppercase, lowercase, digit, symbol).
Natural next steps: wrap the logic in a reusable function, add unit tests, and provide a command-line interface (argparse).