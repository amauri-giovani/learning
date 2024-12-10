def create(db, user,password):
    return f"""
    CREATE USER {user} WITH PASSWORD '{password}';
    GRANT ALL PRIVILEGES ON DATABASE {db} TO {user};
    GRANT ALL ON ALL TABLES IN SCHEMA public to {user};
    GRANT ALL ON ALL SEQUENCES IN SCHEMA public to {user};
    GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to {user};
    CREATE EXTENSION unaccent;
    """

print(create('rocket', 'rocketth', 'rocketth'))
