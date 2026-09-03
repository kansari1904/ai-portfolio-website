const Footer = () => {
  return (
    <footer className="border-t border-slate-900 bg-slate-950">
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div className="flex flex-col gap-6 md:flex-row md:items-center md:justify-between">
          {/* Brand */}
          <div>
            <a
              href="#home"
              className="text-sm font-semibold text-white transition hover:text-slate-300"
            >
              Khalid's Portfolio
            </a>

            <p className="mt-1 text-xs text-slate-600">
              Software Engineer · AI Engineer
            </p>
          </div>

          {/* Social Links */}
          <div className="flex items-center gap-2">
            <a
              href="https://github.com/kansari1904"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="GitHub"
              className="flex h-9 w-9 items-center justify-center rounded-lg border border-slate-800 text-slate-500 transition hover:border-slate-700 hover:bg-slate-900 hover:text-white"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="currentColor"
                className="h-4 w-4"
              >
                <path d="M12 .5C5.65.5.5 5.65.5 12c0 5.08 3.29 9.39 7.86 10.91.57.1.78-.25.78-.55v-2.1c-3.2.7-3.87-1.54-3.87-1.54-.52-1.33-1.28-1.68-1.28-1.68-1.04-.71.08-.7.08-.7 1.15.08 1.76 1.18 1.76 1.18 1.02 1.75 2.68 1.25 3.34.95.1-.74.4-1.25.73-1.54-2.55-.29-5.23-1.28-5.23-5.69 0-1.26.45-2.29 1.18-3.1-.12-.29-.51-1.46.11-3.05 0 0 .96-.31 3.15 1.18a10.9 10.9 0 015.74 0c2.19-1.49 3.15-1.18 3.15-1.18.62 1.59.23 2.76.11 3.05.73.81 1.18 1.84 1.18 3.1 0 4.42-2.69 5.4-5.25 5.68.41.35.78 1.04.78 2.1v3.12c0 .3.21.66.79.55A11.51 11.51 0 0012 23.5C18.35 23.5 23.5 18.35 23.5 12S18.35.5 12 .5z" />
              </svg>
            </a>

            <a
              href="https://www.linkedin.com/in/kansari1904/"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="LinkedIn"
              className="flex h-9 w-9 items-center justify-center rounded-lg border border-slate-800 text-slate-500 transition hover:border-slate-700 hover:bg-slate-900 hover:text-white"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="currentColor"
                className="h-4 w-4"
              >
                <path d="M20.45 20.45h-3.56v-5.57c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.13 1.44-2.13 2.94v5.67H9.35V8.98h3.42v1.56h.05c.48-.9 1.64-1.85 3.38-1.85 3.62 0 4.29 2.38 4.29 5.47v6.29zM5.34 7.41a2.07 2.07 0 110-4.14 2.07 2.07 0 010 4.14zM3.56 20.45h3.56V8.98H3.56v11.47zM22.22 0H1.78C.8 0 .02.78.02 1.75v20.5C.02 23.22.8 24 1.78 24h20.44c.98 0 1.76-.78 1.76-1.75V1.75C23.98.78 23.2 0 22.22 0z" />
              </svg>
            </a>

            <a
              href="mailto:kansari1904@gmail.com"
              aria-label="Email"
              className="flex h-9 w-9 items-center justify-center rounded-lg border border-slate-800 text-slate-500 transition hover:border-slate-700 hover:bg-slate-900 hover:text-white"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.8"
                className="h-4 w-4"
              >
                <rect
                  width="20"
                  height="16"
                  x="2"
                  y="4"
                  rx="2"
                />
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M22 7l-8.97 5.7a2 2 0 01-2.06 0L2 7"
                />
              </svg>
            </a>
          </div>

          {/* Copyright */}
          <p className="text-xs text-slate-600">
            © {new Date().getFullYear()} Khalid Ansari. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;