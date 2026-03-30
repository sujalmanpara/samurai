# Shield Integration Changes

## File 1: `proxy-handler.ts`

### 1. Import (line 18)
Added shield imports after existing key-pool import:
```typescript
import { initShield, scanInput, scanOutput as shieldScanOutput, getShieldConfig } from './shield/index.js';
```

### 2. Input Scan (lines 287–332)
After `parsedBody = JSON.parse(body)`, added full input scanning block:
- Gets shield config for user via `getShieldConfig(keyRecord.user_id)`
- Extracts text from system prompt (string or array format) and all user-role messages (string content or array content blocks)
- Calls `scanInput()` with extracted text, user ID, request ID, and config
- **Block**: returns 403 with `shield_blocked` error, score, and trigger rule IDs
- **Flag**: stores score for `x-shield-score` response header
- **Allow**: continues normally
- Logs shield scan result with score, action, trigger count, and scan time
- Wrapped in try/catch — scan errors are logged but don't block requests

### 3. Shield Score Header (lines 969–971)
Before `res.writeHead()`, adds `x-shield-score` header if the request was flagged.

### 4. Output Scan — Streaming (lines 1004–1006)
After `tryLogUsage()` in the streaming response path, scans the accumulated response via `shieldScanOutput()`. Fire-and-forget (`.catch(() => {})`).

### 5. Output Scan — Non-streaming (lines 1016–1018)
Same as above but in the non-streaming `responseBody` path.

## File 2: `index.ts`

### 1. Import (line 12)
```typescript
import { initShield } from './shield/index.js';
```

### 2. Initialization (line 26)
Added after `initHealthCheck()`:
```typescript
initShield({ dbPath: './data/shield.db' });
```

## Notes
- All imports use `.js` extension (ESM style, matching codebase)
- Edits are surgical — no files rewritten
- Output scan is fire-and-forget to avoid blocking response delivery
- Shield errors are caught and logged, never crash the proxy
