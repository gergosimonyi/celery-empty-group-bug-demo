To run this

```sh
docker run -d -p 6379:6379 redis
uv sync --frozen
uv run manage.py shell
```

Then, in the shell

```python
from root.empty_group_bug import run_all_tasks
run_all_tasks()
```

This will result in

```
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/.../celery-empty-group-bug-demo/root/empty_group_bug.py", line 37, in run_all_tasks
    all_tasks()
    ~~~~~~~~~^^
  File "/.../celery-empty-group-bug-demo/.venv/lib/python3.13/site-packages/celery/canvas.py", line 955, in __call__
    return self.apply_async(args, kwargs)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "/.../celery-empty-group-bug-demo/.venv/lib/python3.13/site-packages/celery/canvas.py", line 1042, in apply_async
    return self.run(args, kwargs, app=app, **(
           ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
        dict(self.options, **options) if options else self.options))
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/.../celery-empty-group-bug-demo/.venv/lib/python3.13/site-packages/celery/canvas.py", line 1067, in run
    tasks, results_from_prepare = self.prepare_steps(
                                  ~~~~~~~~~~~~~~~~~~^
        args, kwargs, self.tasks, root_id, parent_id, link_error, app,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        task_id, group_id, chord, group_index=group_index,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/.../celery-empty-group-bug-demo/.venv/lib/python3.13/site-packages/celery/canvas.py", line 1274, in prepare_steps
    while node.parent:
          ^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'parent'
```
