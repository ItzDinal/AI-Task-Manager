import { ChevronUp, CircleUserRound } from "lucide-react";

// Bottom profile summary with account entry point.
function UserProfileCard() {
  return (
    <button
      type="button"
      className="flex w-full items-center justify-between rounded-2xl border border-gray-200 bg-white p-3 text-left transition-all duration-200 hover:bg-gray-50"
    >
      <div className="flex items-center gap-3">
        <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-gray-100 text-gray-600">
          <CircleUserRound size={18} />
        </div>
        <div>
          <p className="text-sm font-medium text-gray-900">Alex Carter</p>
          <p className="text-xs text-gray-500">alex@aitask.app</p>
        </div>
      </div>
      <ChevronUp size={16} className="text-gray-400" />
    </button>
  );
}

export default UserProfileCard;
