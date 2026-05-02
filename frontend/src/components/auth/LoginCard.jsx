import InputField from "../ui/InputField";
import Button from "../ui/Button";

const LoginCard = () => {
  return (
    <div className="w-full max-w-[450px] rounded-[24px] bg-white p-10 shadow-xl shadow-slate-300/60">
      <h2 className="text-4xl font-bold leading-tight text-[#091f45] lg:text-5xl">Welcome Back</h2>

      <p className="mt-3 text-base text-[#2f5078] lg:text-lg">Let&apos;s get you back into focus.</p>

      <div className="mt-8 space-y-5">
        <InputField label="Email address" type="email" placeholder="sandaru.20232635@iit.ac.lk" />

        <InputField label="Password" type="password" placeholder="•••" />

        <div className="flex items-center justify-between pt-1 text-sm">
          <label className="flex items-center gap-2 text-[#334f73]">
            <input type="checkbox" className="h-4 w-4 rounded border-gray-400 text-blue-600 focus:ring-blue-500" />
            Remember me
          </label>

          <span className="cursor-pointer font-semibold text-blue-600 hover:text-blue-700">Forgot password?</span>
        </div>

        <Button>Log In</Button>

        <div className="flex items-center gap-3 py-2 text-sm text-[#3f5e83]">
          <span className="h-px flex-1 bg-[#d1d9e6]" />
          <span>or continue with</span>
          <span className="h-px flex-1 bg-[#d1d9e6]" />
        </div>

        <div className="flex gap-3">
          <button className="flex flex-1 items-center justify-center gap-2 rounded-xl border border-[#b8c5d8] py-2.5 font-semibold text-[#233b61] transition hover:bg-[#f5f8fd]">
            <span className="text-lg">G</span>
            Google
          </button>
          <button className="flex flex-1 items-center justify-center gap-2 rounded-xl border border-[#b8c5d8] py-2.5 font-semibold text-[#233b61] transition hover:bg-[#f5f8fd]">
            <span className="text-lg">A</span>
            Apple
          </button>
        </div>

        <p className="pt-2 text-center text-sm text-[#3f5e83]">
          Don&apos;t have an account? <span className="cursor-pointer font-semibold text-blue-600 hover:text-blue-700">Sign up</span>
        </p>
      </div>
    </div>
  );
};

export default LoginCard;
