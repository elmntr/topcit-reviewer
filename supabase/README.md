# Account sync setup

The app keeps working without an account and stores guest progress in the current browser. Signing in syncs completed study sessions through Supabase Auth and the `study_progress` table.

1. Create a Supabase project.
2. In **SQL Editor**, run [`setup.sql`](setup.sql).
3. In **Authentication → URL Configuration**, set the Site URL to the deployed Cloudflare Pages URL. Add that exact site URL to the allowed redirect URLs. Add `http://localhost:8080/**` if testing locally.
4. In **Project Settings → API**, copy the Project URL and the publishable key into `js/supabase-config.js`. The publishable key is intended for browser use. Never use the `service_role` key in this app.
5. In Cloudflare Pages, deploy the project root with no build command. The configuration file is part of the static site, so deploy again after editing it.

Email confirmation and password reset both send email. Supabase's built-in email sender is limited to project team addresses and currently allows two emails per hour. For accounts beyond your own testing, configure a custom SMTP provider in Supabase Auth settings before enabling sign-up.

The database table has row-level security policies that restrict each account to its own progress row. Do not remove those policies or disable row-level security.

The Supabase Free plan can pause projects after a week without activity. Progress remains in the database, but sync may be unavailable until the project resumes.
