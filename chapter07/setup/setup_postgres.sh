#!/bin/bash

# Check the operating system
OS=$(uname)

if [ "$OS" == "Darwin" ]; then
    # macOS setup using Homebrew
    echo "Detected macOS. Installing PostgreSQL via Homebrew..."
    brew update
    brew install postgresql
    brew services start postgresql
elif [ -f /etc/debian_version ]; then
    # Debian-based Linux (e.g., Ubuntu)
    echo "Detected Debian-based Linux. Installing PostgreSQL via apt-get..."
    sudo apt-get update
    sudo apt-get install -y postgresql postgresql-contrib
    sudo service postgresql start
else
    echo "Unsupported OS. Please install PostgreSQL manually."
    exit 1
fi

# Switch to the postgres user and execute SQL commands
psql postgres << EOF

-- Create a new database user if it doesn't exist
DO \$\$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_user WHERE usename = 'the_great_coder') THEN
      CREATE USER the_great_coder WITH PASSWORD 'the_great_coder_again';
   END IF;
END
\$\$;

EOF

# Create a new database outside of the DO block
psql postgres << EOF

CREATE DATABASE learn_sql2 OWNER the_great_coder;

EOF

psql postgres << EOF

-- Grant privileges to the user on the database
GRANT ALL PRIVILEGES ON DATABASE learn_sql2 TO the_great_coder;

EOF

echo "PostgreSQL setup completed. Database and user created."
