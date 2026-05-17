import { FolderKanban } from "lucide-react";

const projects = ["Product Roadmap", "Personal Tasks", "Team Sprint"];

// Quick project shortcuts.
function ProjectList() {
  return (
    <section className="space-y-2">
      <p className="px-2 text-xs uppercase tracking-wide text-gray-400">Projects</p>
      <div className="space-y-2">
        {projects.map((project) => (
          <button
            key={project}
            type="button"
            className="flex w-full items-center gap-3 rounded-xl px-4 py-3 text-left text-sm text-gray-600 transition-all duration-200 hover:bg-gray-100"
          >
            <FolderKanban size={16} />
            <span className="truncate">{project}</span>
          </button>
        ))}
      </div>
    </section>
  );
}

export default ProjectList;
