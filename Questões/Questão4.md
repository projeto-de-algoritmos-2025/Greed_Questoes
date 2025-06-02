Claro! Aqui está a descrição da questão **2008. Maximum Earnings From Taxi** no mesmo padrão que você indicou:

---

# 2008. Maximum Earnings From Taxi

[Link para Questão](https://leetcode.com/problems/maximum-earnings-from-taxi/description/)

#### Nível de Dificuldade: MEDIUM

Você está dirigindo um táxi em uma estrada com `n` pontos numerados de 1 a `n`. Seu objetivo é sair do ponto 1 até o ponto `n`, sempre indo para frente, pegando passageiros ao longo do caminho para ganhar dinheiro.

Os passageiros são representados por um array 2D `rides`, onde `rides[i] = [starti, endi, tipi]` indica que o i-ésimo passageiro deseja ser levado do ponto `starti` até o ponto `endi`, oferecendo uma gorjeta de `tipi`.

Se você pegar o passageiro i, você ganha `endi - starti + tipi` dólares.

Você só pode transportar **um passageiro por vez**, mas pode pegar um novo passageiro imediatamente após deixar outro (inclusive no mesmo ponto).

Retorne o **valor máximo em dólares** que você pode ganhar escolhendo os passageiros de forma ótima.

#### Example 1:

Input:
`n = 5, rides = [[2,5,4],[1,5,1]]`
Output:
`7`
Explanation:
Pegamos o passageiro 0 e ganhamos 5 - 2 + 4 = 7 dólares.

#### Example 2:

Input:
`n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]`
Output:
`20`
Explanation:
Selecionamos os passageiros:

* Passageiro 1: do ponto 3 ao 10, ganho de 10 - 3 + 2 = 9
* Passageiro 2: do ponto 10 ao 12, ganho de 12 - 10 + 3 = 5
* Passageiro 5: do ponto 13 ao 18, ganho de 18 - 13 + 1 = 6
  Total: 9 + 5 + 6 = 20

#### Constraints:

* 1 <= n <= 10⁵
* 1 <= rides.length <= 3 × 10⁴
* rides\[i].length == 3
* 1 <= starti < endi <= n
* 1 <= tipi <= 10⁵

#### Text Result:

![Submissions](imagens/TR_Questao2008.png)

