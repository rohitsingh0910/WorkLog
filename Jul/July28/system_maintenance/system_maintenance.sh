#!/bin/bash
# System Health + Log Cleaner Script

# === CONFIGURATIONS ===
THRESHOLD=80
LOG_DIR="./sample_logs"
LOG_RETENTION_DAYS=7
LOG_OUTPUT_DIR="./logs"
mkdir -p "$LOG_OUTPUT_DIR"

# === TIMESTAMP ===
TIMESTAMP=$(date "+%Y-%m-%d_%H-%M-%S")
REPORT_FILE="$LOG_OUTPUT_DIR/system_report_$TIMESTAMP.txt"

# === DISK USAGE ===
disk_usage=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

echo "📦 DISK USAGE: $disk_usage%" | tee -a "$REPORT_FILE"
if [ "$disk_usage" -gt "$THRESHOLD" ]; then
    echo "⚠️ Disk usage is above $THRESHOLD%. Cleaning logs older than $LOG_RETENTION_DAYS days..." | tee -a "$REPORT_FILE"
    find "$LOG_DIR" -type f -name "*.log" -mtime +$LOG_RETENTION_DAYS -exec rm -f {} \;
    echo "✅ Old logs deleted." | tee -a "$REPORT_FILE"
else
    echo "✅ Disk usage is under control." | tee -a "$REPORT_FILE"
fi

# === CPU USAGE ===
cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
echo "🧠 CPU Usage: $cpu_usage%" | tee -a "$REPORT_FILE"

# === MEMORY USAGE ===
mem_usage=$(free -m | awk 'NR==2{printf "💾 Memory Usage: %s/%sMB (%.2f%%)\n", $3,$2,$3*100/$2 }')
echo "$mem_usage" | tee -a "$REPORT_FILE"

# === COMPLETION ===
echo "✅ System maintenance completed at $TIMESTAMP" | tee -a "$REPORT_FILE"
