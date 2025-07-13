"use client";

export interface Todo {
  id: number;
  title: string;
  completed: boolean;
}

export default function TodoItem({
  todo,
  onToggleComplete,
  onDelete,
}: {
  todo: Todo;
  onToggleComplete: (id: number, completed: boolean) => void;
  onDelete: (id: number) => void;
}) {
  return (
    <li
      className={`flex items-center justify-between p-4 rounded-lg ${
        todo.completed ? "bg-gray-200 text-gray-500" : "bg-white"
      }`}
    >
      <span
        className={`cursor-pointer ${
          todo.completed ? "line-through" : ""
        }`}
        onClick={() => onToggleComplete(todo.id, !todo.completed)}
      >
        {todo.title}
      </span>
      <button
        onClick={() => onDelete(todo.id)}
        className="px-3 py-1 text-sm font-semibold text-white bg-red-500 rounded-full hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
      >
        Delete
      </button>
    </li>
  );
}
