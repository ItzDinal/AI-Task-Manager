import sys
import os
sys.path.insert(0, os.path.abspath('.'))

results = {}

for name, code in [
    ('config', 'from app.core.config import settings; results["config"] = settings.DATABASE_URL[:20]'),
    ('auth_service', 'from app.services.auth_service import create_user; results["auth_service"] = True'),
    ('security', 'import app.core.security as security; results["security"] = [a for a in dir(security) if a in ("hash_password", "verify_password", "create_access_token")]'),
    ('auth_route', 'import app.api.v1.auth as auth; results["auth_route"] = hasattr(auth, "router")'),
    ('user', 'from app.models.user import User; results["user"] = User.__tablename__'),
]:
    try:
        exec(code)
    except Exception as e:
        results[name] = ('ERROR', type(e).__name__, str(e))

print(results)
