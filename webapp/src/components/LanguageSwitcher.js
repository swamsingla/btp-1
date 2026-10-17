import Link from 'next/link';
import { LANGUAGES } from '@/lib/content';

/**
 * Offers the languages this page has actually been generated in.
 *
 * Driven by what is on disk rather than by a fixed list, so it can never link to a
 * page that does not exist — pages are generated concept by concept, and most concepts
 * have none yet. With only one language available there is nothing to switch between,
 * so it renders nothing.
 */
export default function LanguageSwitcher({ available, current, basePath }) {
  if (!available || available.length < 2) return null;

  return (
    <div className="flex items-center gap-2 flex-wrap mb-6">
      <span className="text-xs text-gray-400 dark:text-gray-500 uppercase tracking-wider mr-1">
        Read in
      </span>
      {available.map((code) => {
        const isCurrent = code === current;
        // English is the default, so it needs no query parameter.
        const href = code === 'en' ? basePath : `${basePath}?lang=${code}`;
        return (
          <Link
            key={code}
            href={href}
            lang={code === 'od' ? 'or' : code}
            aria-current={isCurrent ? 'page' : undefined}
            className={`px-3 py-1.5 rounded-lg border text-sm transition-all ${
              isCurrent
                ? 'bg-blue-600 text-white border-blue-600 shadow-sm'
                : 'bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700 ' +
                  'text-gray-600 dark:text-gray-300 hover:border-blue-300 hover:text-blue-600'
            }`}
          >
            {LANGUAGES[code]?.native ?? code}
          </Link>
        );
      })}
    </div>
  );
}
