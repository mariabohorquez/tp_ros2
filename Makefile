shell:
	sudo docker compose up -d
	sudo docker compose exec ros2 bash -ic "cd /root/ros2_ws && test -d install/bohorquez_hernandez_tp2_pkg || colcon build"
	sudo docker compose exec ros2 bash

attach:
	sudo docker exec -it tp_ros2 bash

rebuild:
	sudo docker compose down
	sudo docker compose up -d
	sudo docker compose exec ros2 bash -ic "cd /root/ros2_ws && colcon build"

down:
	sudo docker compose down
