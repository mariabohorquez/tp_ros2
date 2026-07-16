# TP3: localización espacial (TF2)

Nodo que consulta la transformación entre `base_link` y `tool0` del doble péndulo (paquete
`clase3` del curso) e imprime la matriz de rototraslación SE(3).

## Idea

El sistema publica las transformaciones como traslación + cuaternión en `/tf`. El nodo:

1. Escucha `/tf` con un `Buffer` y un `TransformListener`.
2. Pide `lookup_transform('base_link', 'tool0')`, que devuelve la pose de `tool0` vista desde
   `base_link` (o sea, la transformación base -> tool).
3. Convierte el cuaternión a matriz de rotación 3x3 y arma la SE(3) 4x4 con la traslación.

La consulta corre en un timer de 1 s, así que si movés los sliders del `joint_state_publisher_gui`
la matriz se actualiza.

## Correr

El paquete `clase3` (doble péndulo) es del curso y vive en el repo `fros`, así que esto se corre
en un workspace que tenga clase3 + este paquete.

Todo junto con un solo launch (doble péndulo + RViz + sliders + el nodo):

```bash
ros2 launch bohorquez_durante_tp3_pkg tp3.launch.py
```

O por separado, si el sistema ya está levantado:

```bash
ros2 launch clase3 dp_launch.py               # una terminal
ros2 run bohorquez_durante_tp3_pkg base_tool_tf   # otra terminal
```

## Build

```bash
colcon build --packages-select bohorquez_durante_tp3_pkg
source install/setup.bash
```
