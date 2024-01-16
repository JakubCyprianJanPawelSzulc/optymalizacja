import networkx as nx
import matplotlib.pyplot as plt


class Task:
    def __init__(self, duration, dependencies):
        self.duration = duration
        self.dependencies = dependencies
        self.earliest_start = 0
        self.earliest_finish = 0
        self.latest_start = float('inf')
        self.latest_finish = float('inf')

    def __str__(self):
        return f"ES: {self.earliest_start}, EF: {self.earliest_finish}, LS: {self.latest_start}, LF: {self.latest_finish}"


def is_graph_acyclic(tasks):
    G = nx.DiGraph()

    for index, task in enumerate(tasks):
        G.add_node(chr(ord('A') + index))

        for dependency in task.dependencies:
            G.add_edge(chr(ord('A') + dependency), chr(ord('A') + index))

    return nx.is_directed_acyclic_graph(G)


def calculate_early_start_finish(tasks):
    for task in tasks:
        if not task.dependencies:
            task.earliest_start = 0
            task.earliest_finish = task.duration
        else:
            task.earliest_start = max(tasks[dependency].earliest_finish for dependency in task.dependencies)
            task.earliest_finish = task.earliest_start + task.duration


def calculate_late_start_finish(tasks):
    for task in reversed(tasks):
        if tasks.index(task) == len(tasks) - 1:
            task.latest_finish = task.earliest_finish
            task.latest_start = task.latest_finish - task.duration
        else:
            depending_tasks = [t for t in tasks if tasks.index(task) in t.dependencies]
            if depending_tasks:
                task.latest_finish = min(t.latest_start for t in depending_tasks)
                task.latest_start = task.latest_finish - task.duration


def find_critical_path(tasks):
    return [tasks.index(task) for task in tasks if task.earliest_start == task.latest_start and task.earliest_finish == task.latest_finish]


def gantt_chart(tasks):
    task_names = [chr(ord('A') + index) for index in range(len(tasks))]
    task_starts = [task.earliest_start for task in tasks]
    task_durations = [task.duration for task in tasks]

    fig, ax = plt.subplots()

    ax.barh(task_names, task_durations, left=task_starts, color='green')
    ax.set_xlabel('Czas')
    ax.set_ylabel('Zadania')
    ax.set_title('Diagram Gantta')

    plt.show()


def visualize_graph(tasks):
    G = nx.DiGraph()

    for index, task in enumerate(tasks):
        node_label = f"{chr(ord('A') + index)}\nES: {task.earliest_start}\nEF: {task.earliest_finish}\nLS: {task.latest_start}\nLF: {task.latest_finish}"
        G.add_node(chr(ord('A') + index), label=node_label)

        for dependency in task.dependencies:
            G.add_edge(chr(ord('A') + dependency), chr(ord('A') + index))

    pos = nx.shell_layout(G)
    node_labels = nx.get_node_attributes(G, 'label')

    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightblue', font_size=8, labels=node_labels, edge_color='red')
    plt.show()


def main():
    tasks = [
        Task(0.5, []),
        Task(1, [0]),
        Task(5, [1]),
        Task(3, [2]),
        Task(4, [1]),
        Task(3, [1]),
        Task(0.5, [2]),
        Task(0.5, [3, 4, 5]),
        Task(0.5, [6, 7]),
    ]

    if is_graph_acyclic(tasks):
        print("Graf jest acykliczny")
    else:
        print("Graf zawiera cykle")

    calculate_early_start_finish(tasks)
    calculate_late_start_finish(tasks)

    for task in tasks:
        print(f"{chr(ord('A') + tasks.index(task))}: {task}")

    critical_path = find_critical_path(tasks)
    print(f"\nŚcieżka krytyczna: {critical_path}")

    visualize_graph(tasks)
    gantt_chart(tasks)


if __name__ == "__main__":
    main()
