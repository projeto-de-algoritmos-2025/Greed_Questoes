# 2054. Two Best Non-Overlapping Events

[Link para Questão](https://leetcode.com/problems/two-best-non-overlapping-events/description/)

#### Nível de Dificuldade: MEDIUM

Dado um array 2D `events`, onde `events[i] = [startTimei, endTimei, valuei]`, representando que o evento `i` começa em `startTimei`, termina em `endTimei`, e tem valor `valuei`, você pode participar de **no máximo dois eventos não sobrepostos**.

O tempo de início e fim são inclusivos. Ou seja, se você participa de um evento que termina no tempo `t`, o próximo evento só pode começar no tempo `t + 1` ou depois.

Retorne a **maior soma de valores** possível participando de no máximo dois eventos **não sobrepostos**.

#### Example 1:

Input:
`events = [[1,3,2],[4,5,2],[2,4,3]]`
Output:
`4`
Explanation:
Escolha os eventos 0 e 1, com valores 2 + 2 = 4.

#### Example 2:

Input:
`events = [[1,3,2],[4,5,2],[1,5,5]]`
Output:
`5`
Explanation:
Escolha apenas o evento 2 com valor 5.

#### Example 3:

Input:
`events = [[1,5,3],[1,5,1],[6,6,5]]`
Output:
`8`
Explanation:
Escolha os eventos 0 e 2, com valores 3 + 5 = 8.

#### Constraints:

* 2 <= events.length <= 10⁵
* events\[i].length == 3
* 1 <= startTimei <= endTimei <= 10⁹
* 1 <= valuei <= 10⁶

#### Text Result:

![Submissions](imagens/Solução_3.png)

