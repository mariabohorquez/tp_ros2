# TP de ROS 2: Fundamentos de Robótica (FIUBA)

Entregas del curso, en ROS 2 Jazzy.

- **[tp1/](tp1/)**: reproduce un rosbag (robot corriendo) en RViz y RQT con un solo launch.
- **[tp2/](tp2/)**: servicios y parámetros (contador) + action (republicador).

## Cómo correr

El entorno es la imagen del curso (ROS 2 Jazzy). El `docker-compose.yaml` la levanta y monta
este repo como workspace. Origen de la imagen: https://github.com/pgonfiuba/fros

Lo más rápido es con `make` (hace falta `docker`, `docker compose` y `make`):

```bash
make rebuild   # la primera vez: crea el contenedor y compila
make shell     # entra al contenedor (ROS y el workspace ya sourceados)
make down      # lo baja al terminar
```

Ya adentro corrés el ejercicio que quieras:

```bash
ros2 launch bohorquez_hernandez_tp2_pkg contador.launch.py
ros2 launch bohorquez_hernandez_tp2_pkg republicador.launch.py
```

O todo a mano:

```bash
# levantar el contenedor
sudo HOME="$HOME" XAUTHORITY="$XAUTHORITY" DISPLAY="$DISPLAY" docker compose up -d
sudo docker exec -it tp_ros2 bash

# dentro del contenedor:
source /opt/ros/jazzy/setup.bash
cd /root/ros2_ws
colcon build
source install/setup.bash
```

Con el workspace compilado:

```bash
# TP1 (rosbag + RViz + RQT) -- ver tp1/README.md para bajar el rosbag
ros2 launch bohorquez_hernandez_pkg bag_demo.launch.py
# TP2 - ejercicio 1 (contador + servicio)
ros2 launch bohorquez_hernandez_tp2_pkg contador.launch.py
# TP2 - ejercicio 2 (republicador con action)
ros2 launch bohorquez_hernandez_tp2_pkg republicador.launch.py
```

Para bajar el contenedor:

```bash
sudo HOME="$HOME" XAUTHORITY="$XAUTHORITY" DISPLAY="$DISPLAY" docker compose down
```

