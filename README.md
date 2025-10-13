# optimal-blocks-timeout
Este repositorio contiene un script para calcular el **tiempo óptimo $T_{opt}$** para enviar bloques de votos a la blockchain, usando la distribución de Poisson para modelar la llegada de votos.

---

## Archivo principal

- `timeopt.py` : Script en Python que calcula $T_{opt}$ para un bloque de tamaño `k` y una tolerancia `epsilon`.

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

- Se usa **búsqueda binaria** para hallar μ tal que $P(X \leq k-1) = \varepsilon$, donde $X \sim Poisson(\mu)$.
- Luego, el tiempo óptimo se calcula como:

$$
T_{opt} = \frac{\mu}{\lambda}, \quad \lambda = \frac{N}{1440} \text{ votos por minuto}
$$

- La probabilidad de que el bloque se llene se calcula con la función de distribución acumulada de Poisson (`poisson.cdf` de `scipy`).

---

## Notas

- La tolerancia `epsilon` se fija en 0.01 por defecto, pero puede modificarse según necesidad.
- El script está pensado para **simular bloques de mix-nodes** en sistemas de votación electrónica.
