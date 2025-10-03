#!/bin/bash

read -p "Enter a choice [start|stop|restart]: " input

case $input in
  start)
    echo "Starting service..."
    ;;
  stop)
    echo "Stopping service..."
    ;;
  restart)
    echo "Restarting service..."
    ;;
  *)
    echo "Invalid option"
    ;;
esac
