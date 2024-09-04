#!/bin/bash

# Function to print section headers
print_header() {
    echo "========================================"
    echo "$1"
    echo "========================================"
}

# Stop and remove Docker containers
print_header "Stopping and removing Docker containers"
docker-compose down -v
docker rm -f $(docker ps -aq)

# Remove Kafka data
print_header "Removing Kafka data"
rm -rf /tmp/kafka-logs /tmp/zookeeper

# MongoDB cleanup
print_header "Cleaning up MongoDB"
mongo <<EOF
show dbs
var dbs = db.adminCommand('listDatabases').databases;
dbs.forEach(function(database) {
    if (database.name != 'admin' && database.name != 'config' && database.name != 'local') {
        db = db.getSiblingDB(database.name);
        db.dropDatabase();
        print("Dropped database: " + database.name);
    }
});
EOF

# PostgreSQL cleanup
print_header "Cleaning up PostgreSQL"
sudo -u postgres psql <<EOF
\list
DROP DATABASE IF EXISTS your_database_name;
\list
EOF

print_header "Cleanup complete"