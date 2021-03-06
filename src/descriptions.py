
def help():
  return ('\n'
        + 'usage: bullet [--help|help]                                                     (0)\n'
        + '       bullet init                                                              (1)\n'
        + '       bullet new task [<title>] [<body>...]                                    (2)\n'
        + '       bullet new subtask <task_id> [<title>] [<body>...]                       (3)\n'
        + '       bullet delete (task|subtask) <bullet_id> [--confirm|confirm]             (4)\n'
        + '       bullet (<command>) <task_id> [<args>...]                                 (5)\n'
        + '       bullet set (task|subtask) <bullet_id> (<attribute>) <val>                (6)\n'
        + '       bullet show [--all|--relevant|--unfinished|--<filter> [<args>]...]...    (7)\n'
        + '\n'
        + '(0) view this help message\n'
        + '\n'
        + '(1) create a new bullet-backlog in this directory\n'
        + '\n'
        + '(2) create a new task\n'
        + '    ○ if no arguments provided, title and body will be prompted\n'
        + '    ○ if only one argument <arg> is provided, title=<arg> and body will be prompted\n'
        + '    ex: bullet new task sample_title this is a sample body\n'
        + '\n'
        + '(3) create a new subtask under task <task_id>\n'
        + '    ○ if no arguments provided, title and body will be prompted\n'
        + '    ○ if only one argument <arg> is provided, title=<arg> and body will be prompted\n'
        + '    ex: bullet new subtask 1\n'
        + '\n'
        + '(4) delete an existing bullet\n'
        + '    ○ if confirmation not provided, confirmation will be prompted\n'
        + '    ex: bullet delete subtask 4 --confirm\n'
        + '\n'
        + '(5) add relations/tags to an existing task <task_id>\n'
        + '    ○ commands: tag, untag, parent, unparent, child, unchild\n'
        + '    ○ tag: an attribute of a task\n'
        + '    ○ parent: if task <a> is a parent of task <b>, then <b> relies on <a>\n'
        + '    ○ child: if task <a> is a child of task <b>, then <a> relies on <b>\n'
        + '    ex: bullet tag 2 python sql cli\n'
        + '\n'
        + '(6) edit attribute values for an existing bullet <bullet_id>\n'
        + '    ○ attributes: title, body, status, level, startdate, enddate, location\n'
        + '    ○ level: an integer representing the importance of a bullet\n'
        + '       ○ 0: none\n'
        + '       ○ 1: low\n'
        + '       ○ 2: normal\n'
        + '       ○ 3: high\n'
        + '       ○ 4: critical\n'
        + '    ○ status: an integer representing the progress status of a bullet\n'
        + '       ○ 0: none\n'
        + '       ○ 1: incomplete\n'
        + '       ○ 2: todo\n'
        + '       ○ 3: in progress\n'
        + '       ○ 4: complete\n'
        + '    ex: bullet set task 2 status 3\n'
        + '\n'
        + '(7) visualize bullets in the terminal with stacking filters\n'
        + '    ○ filters: --all, --relevant, --unfinished, --tags_any, --tags_all, location\n'
        + '    ○ --all: show all tasks\n'
        + '    ○ --relevant: filter out tasks whose parents are not complete\n'
        + '    ○ --unfinished: filter out finished tasks\n'
        + '    ○ --tags_any: only show tasks with any of the specified tags\n'
        + '    ○ --tags_all: only show tasks with at least all of the specified tags\n'
        + '    ○ --location: only show tasks with any of the specified locations\n'
        + '')

