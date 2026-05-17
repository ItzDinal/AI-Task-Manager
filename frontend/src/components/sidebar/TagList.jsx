const tags = [
  { label: "Deep Work", tone: "bg-gray-200" },
  { label: "Quick Wins", tone: "bg-gray-300" },
  { label: "AI Review", tone: "bg-gray-400" },
];

// Tag and category shortcuts.
function TagList() {
  return (
    <section className="space-y-2">
      <p className="px-2 text-xs uppercase tracking-wide text-gray-400">Tags</p>
      <div className="space-y-2">
        {tags.map((tag) => (
          <button
            key={tag.label}
            type="button"
            className="flex w-full items-center gap-3 rounded-xl px-4 py-3 text-left text-sm text-gray-600 transition-all duration-200 hover:bg-gray-100"
          >
            <span className={`h-2.5 w-2.5 rounded-full ${tag.tone}`} />
            <span>{tag.label}</span>
          </button>
        ))}
      </div>
    </section>
  );
}

export default TagList;
