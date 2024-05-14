#!/usr/bin/env python3

from pymongo import MongoClient


def main():
    """Connects to MongoDB, retrieves and prints statistics about Nginx logs."""

    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Get total number of documents
    count = collection.count_documents({})

    # Print total document count
    print(f"{count} logs")

    # Define methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Count documents for each method
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    # Print method counts
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")

    # Count documents with specific method and path
    status_checks = collection.count_documents({"method": "GET", "path": "/status"})

    # Print status check count
    print(f"{status_checks} status check")


if __name__ == "__main__":
    main()

