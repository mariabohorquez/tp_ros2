shell:
	sudo docker compose up -d
	sudo docker compose exec ros2 bash

attach:
	sudo docker exec -it tp_ros2 bash

rebuild:
	sudo docker compose down
	sudo docker compose up -d
	@echo "compilando (entrypoint)..."
	@while ! sudo docker logs tp_ros2 2>&1 | grep -q "Summary:"; do sleep 2; done
	@echo "listo"

down:
	sudo docker compose down
