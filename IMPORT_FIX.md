# 🔧 导入错误修复

## ❌ 错误信息

```
NameError: name 'Tuple' is not defined. Did you mean: 'tuple'?
```

## 🔍 原因

在 `backend/api.py` 中添加了 `_llm_filter_concepts()` 函数，使用了 `Tuple` 类型注解：

```python
async def _llm_filter_concepts(candidates: List[Tuple[str, int]], client, target_count: int = 30) -> List[Tuple[str, int]]:
```

但忘记导入 `Tuple` 类型。

## ✅ 修复

在 `backend/api.py` 第11行，添加 `Tuple` 到导入语句：

**改前**：
```python
from typing import List, Dict, Optional
```

**改后**：
```python
from typing import List, Dict, Optional, Tuple
```

## 🎯 验证

修复后，服务器会自动重载并正常启动。

后端日志应该显示：
```
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## 📝 状态

- ✅ 已修复
- ✅ 无 linter 错误
- ✅ 服务器自动重载

**修复时间**：2025-12-20

