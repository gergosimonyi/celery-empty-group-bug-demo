from celery import chain, group

from root.celery import debug_task


# We want to queue many tasks in 3 groups. Tasks in the same group can be run
# in parallel, but the first group must be done before the second group starts
# and the second group must be done before the third group starts.


def get_group_one():
    # Happens to return 2 tasks.
    return [
        debug_task.si(),
        debug_task.si(),
    ]


def get_group_two():
    # Happens to return 0 tasks.
    return []


def get_group_three():
    # Happens to return 0 tasks.
    return []


def run_all_tasks():
    all_tasks = chain(
        group(get_group_one()),
        group(get_group_two()),
        group(get_group_three()),
    )

    # Throws!
    all_tasks()
