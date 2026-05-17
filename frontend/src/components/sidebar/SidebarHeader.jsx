import { Sparkles } from "lucide-react";

// Brand header section for product identity.
function SidebarHeader() {
  return (
    <div className="rounded-2xl border border-gray-200 bg-gray-50 p-4">
      <div className="flex items-center gap-3">
        <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-black text-white">
          <Sparkles size={16} />
        </div>
        <div>
          <p className="text-sm font-semibold text-gray-900">AI Task Manager</p>
          <p className="text-xs text-gray-500">Focus-first workspace</p>
        </div>
      </div>
    </div>
  );
}

export default SidebarHeader;
