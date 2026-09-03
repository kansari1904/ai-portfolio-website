import { useState } from "react";

const Navbar = () => {
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    const navLinks = [
        { name: "Home", href: "#home" },
        { name: "Chat", href: "#chat" },
        { name: "About", href: "#about" },
        { name: "Contact", href: "#contact" },
    ];

    return (
        <nav className="fixed left-0 top-0 z-50 w-full border-b border-slate-800 bg-slate-950 text-white">
            <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">

                {/* Logo */}
                <a
                    href="#home"
                    className="text-lg font-semibold tracking-tight sm:text-xl"
                >
                    Khalid's Portfolio
                </a>

                {/* Desktop Navigation */}
                <div className="hidden items-center gap-8 md:flex">
                    {navLinks.map((link) => (
                        <a
                            key={link.name}
                            href={link.href}
                            className="text-sm font-medium text-slate-300 transition-colors duration-200 hover:text-white"
                        >
                            {link.name}
                        </a>
                    ))}
                </div>

                {/* Mobile Menu Button */}
                <button
                    type="button"
                    onClick={() => setIsMenuOpen(!isMenuOpen)}
                    className="rounded-md p-2 text-slate-300 transition hover:bg-slate-800 hover:text-white md:hidden"
                    aria-label="Toggle navigation menu"
                    aria-expanded={isMenuOpen}
                >
                    {isMenuOpen ? (
                        /* Close icon */
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            className="h-6 w-6"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                            strokeWidth={2}
                        >
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                d="M6 18L18 6M6 6l12 12"
                            />
                        </svg>
                    ) : (
                        /* Hamburger icon */
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            className="h-6 w-6"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                            strokeWidth={2}
                        >
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                d="M4 6h16M4 12h16M4 18h16"
                            />
                        </svg>
                    )}
                </button>
            </div>

            {/* Mobile Navigation */}
            {isMenuOpen && (
                <div className="border-t border-slate-800 bg-slate-950 md:hidden">
                    <div className="mx-auto max-w-7xl px-4 py-4 sm:px-6">
                        <div className="flex flex-col space-y-1">
                            {navLinks.map((link) => (
                                <a
                                    key={link.name}
                                    href={link.href}
                                    onClick={() => setIsMenuOpen(false)}
                                    className="rounded-md px-3 py-3 text-sm font-medium text-slate-300 transition-colors duration-200 hover:bg-slate-900 hover:text-white"
                                >
                                    {link.name}
                                </a>
                            ))}
                        </div>
                    </div>
                </div>
            )}
        </nav>
    );
};

export default Navbar;