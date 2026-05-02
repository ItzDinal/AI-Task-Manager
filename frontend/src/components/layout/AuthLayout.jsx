const AuthLayout = ({ left, right }) => {
  return (
    <div className="min-h-screen bg-[#e9edf4] lg:flex">
      {/* LEFT */}
      <div className="flex w-full flex-col justify-center px-6 py-10 sm:px-10 lg:w-1/2 lg:px-16">
        {left}
      </div>

      {/* RIGHT */}
      <div className="flex w-full items-center justify-center px-6 pb-10 sm:px-10 lg:w-1/2 lg:px-16 lg:py-10">
        {right}
      </div>
    </div>
  );
};

export default AuthLayout;
