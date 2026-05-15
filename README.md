# optimal-blocks-timeout

This repository contains a script to compute the optimal time `T_opt` for sending vote blocks to the blockchain, using the Poisson distribution to model the arrival of votes.

## Main File

- `timeopt.py`: Python script that computes `T_opt` for a block of size `k` and a tolerance `ε`.

## How to Use

1. Make sure you have Python 3 installed.

2. Install the `scipy` library if you do not already have it:

```bash
pip install scipy
```

3. Run the script from the terminal or from your IDE:

```bash
python timeopt.py
```

The script will ask for:

- `N`: total number of votes per node
- `k`: size of the vote block

The script will output:

- `T`: optimal time (in minutes) to fill a block with probability `1-ε`
- The probability that the block is filled within that time

## Algorithm Explanation

Binary search is used to find μ such that

```text
P(X ≤ k - 1) = ε
```

where

```text
X ~ Poisson(μ)
```

The optimal time is then computed as

```text
T_opt = μ / λ
λ = N / 1440 votes per minute
```

The probability that the block is filled is computed using the cumulative distribution function of the Poisson distribution (`poisson.cdf` from `scipy`).

## Notes

- The tolerance `ε` is set to 0.01 by default, but it can be modified as needed.
- The script is intended to simulate mix-node blocks in electronic voting systems.
Este repositorio contiene un script para calcular el **tiempo óptimo $T_{opt}$** para enviar bloques de votos a la blockchain, usando la distribución de Poisson para modelar la llegada de votos.

---
# optimal-blocks-timeout (Spanish)
## Archivo principal

- `timeopt.py` : Script en Python que calcula `T_opt` para un bloque de tamaño `k` y una tolerancia `epsilon`.

---

## Cómo usar

1. Asegúrate de tener Python 3 instalado.
2. Instala la librería **scipy** si no la tienes:
    ```bash
    pip install scipy
    ```
3. Ejecuta el script desde la terminal o tu IDE:
    ```bash
    python timeopt.py
    ```
4. El script pedirá ingresar:
    - `N` : número total de votos por nodo
    - `k` : tamaño del bloque de votos
5. El resultado que imprime será:
    - `T` : tiempo óptimo (en minutos) para llenar un bloque con probabilidad `1 - epsilon`
    - Probabilidad de que el bloque se llene en ese tiempo

---


## Explicación del algoritmo

- Se usa **búsqueda binaria** para hallar `μ` tal que
 ```text
P(X ≤ k - 1) = ε
```
donde
```text
X ~ Poisson(μ)
```
- Luego, el tiempo óptimo se calcula como:

```text
T_opt = μ / λ
λ = N / 1440 votes per minute
```

- La probabilidad de que el bloque se llene se calcula con la función de distribución acumulada de Poisson (`poisson.cdf` de `scipy`).

---

## Notas

- La tolerancia `epsilon` se fija en 0.01 por defecto, pero puede modificarse según necesidad.
- El script está pensado para **simular bloques de mix-nodes** en sistemas de votación electrónica.
