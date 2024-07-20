import os
import random
from git import Repo
from datetime import datetime, timedelta
import pytz

# Initialize Git repository
repo = Repo.init('.')
index = repo.index

# Define date range for past 3 years
start_date = datetime.now() - timedelta(days=365 * 3)
end_date = datetime.now()
total_days = (end_date - start_date).days

# Open test.txt for writing
with open('test.txt', 'w') as file:
    # Loop over a percentage of days in the three-year period
    for _ in range(int(total_days * 0.75)):
        # Generate a random day within the three-year period
        random_day = start_date + timedelta(days=random.randint(0, total_days))
        # Generate a random number of commits for the selected day, between 5 and 50
        num_commits = random.randint(1, 20)
        for _ in range(num_commits):
            # Generate random commit time within the selected day
            commit_time = random_day + timedelta(seconds=random.randint(0, 86400))
            # Add timezone information
            commit_time = pytz.utc.localize(commit_time)
            # Write commit time to test.txt
            file.write(str(commit_time) + '\n')
            # Commit changes with author date
            index.commit('Commit ' + str(commit_time), author_date=commit_time)

# Add the file once
index.add(['test.txt'])

# Push to origin
origin = repo.remote(name='origin')
origin.push(refspec='main')     