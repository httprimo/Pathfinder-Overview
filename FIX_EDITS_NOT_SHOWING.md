# Fix: Edits Not Showing on Website

## The Problem
In Laravel + Vite applications, **you MUST run the Vite development server** for your edits to appear. Vite compiles your Vue/JavaScript/CSS files on-the-fly.

## Quick Fix

### For Development (Recommended)

**You need TWO terminals running:**

**Terminal 1 - Vite Dev Server (MUST BE RUNNING):**
```bash
npm run dev
```
Keep this running! This compiles your assets and enables hot module replacement.

**Terminal 2 - Laravel Server:**
```bash
php artisan serve
```

**Then visit:** `http://localhost:8000`

### For Production

If you're deploying or need production builds:
```bash
npm run build
php artisan serve
```

## Complete Troubleshooting Steps

### Step 1: Clear All Caches

Run these commands:

```bash
# Clear Vite cache
rm -rf node_modules/.vite

# Clear Laravel caches
php artisan view:clear
php artisan config:clear
php artisan route:clear
php artisan cache:clear
```

**Windows PowerShell:**
```powershell
Remove-Item -Recurse -Force node_modules\.vite -ErrorAction SilentlyContinue
php artisan view:clear
php artisan config:clear
php artisan route:clear
php artisan cache:clear
```

**Windows CMD:**
```cmd
rmdir /s /q node_modules\.vite 2>nul
php artisan view:clear
php artisan config:clear
php artisan route:clear
php artisan cache:clear
```

### Step 2: Verify Node Modules

Make sure dependencies are installed:
```bash
npm install
```

### Step 3: Start Both Servers

**Terminal 1:**
```bash
npm run dev
```
You should see something like:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

**Terminal 2:**
```bash
php artisan serve
```
You should see:
```
  INFO  Server running on [http://127.0.0.1:8000]
```

### Step 4: Hard Refresh Browser

1. Open Developer Tools (F12)
2. Right-click the refresh button
3. Select "Empty Cache and Hard Reload"
   
   OR
   
   Press: `Ctrl + Shift + R` (Windows/Linux) or `Cmd + Shift + R` (Mac)

### Step 5: Check Browser Console

1. Open Developer Tools (F12)
2. Go to Console tab
3. Look for errors - if you see "Failed to fetch" or connection errors, Vite isn't running
4. Check Network tab - assets should load from `localhost:5173` (Vite server)

## Common Issues

### Issue: "Failed to fetch" or "Connection refused"
**Solution:** Make sure `npm run dev` is running in Terminal 1

### Issue: Still seeing old content
**Solution:** 
- Stop both servers (Ctrl+C)
- Clear caches (Step 1)
- Restart both servers (Step 3)
- Hard refresh browser (Step 4)

### Issue: "VITE not found" or "command not found"
**Solution:** 
```bash
npm install
```

### Issue: Port already in use
**Solution:** 
```bash
# Kill process on port 5173 (Vite default)
# Windows:
netstat -ano | findstr :5173
taskkill /PID <PID> /F

# Then restart npm run dev
```

## Development Workflow

1. **Always start with:** `npm run dev` (keep running)
2. **Then start:** `php artisan serve` (keep running)
3. **Make your edits** to `.vue`, `.js`, or `.css` files
4. **Save the file** - Vite will automatically recompile
5. **Browser will auto-refresh** (hot module replacement)

## Verification Checklist

- [ ] `npm run dev` is running and shows "VITE ready"
- [ ] `php artisan serve` is running and shows "Server running"
- [ ] Browser console has no errors
- [ ] Network tab shows assets loading from Vite server (port 5173)
- [ ] Hard refreshed browser (Ctrl+Shift+R)
- [ ] Caches cleared

## Still Not Working?

1. Check that you're editing files in `resources/js/` or `resources/css/`
2. Verify file syntax is correct (no JavaScript/Vue errors)
3. Try incognito/private browser window
4. Check if antivirus/firewall is blocking Vite server
5. Verify Node.js version: `node --version` (should be 16+)

