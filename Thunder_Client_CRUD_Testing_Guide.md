# Thunder Client CRUD Operations Testing Guide

## 📋 Overview
This guide provides detailed steps to test all CRUD (Create, Read, Update, Delete) operations for the Emotion Analysis API using Thunder Client in VS Code.

## 🚀 Prerequisites
1. **Install Thunder Client Extension** in VS Code
2. **Start the FastAPI Server**: 
   ```bash
   python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
3. **Base URL**: `http://localhost:8000`

## 📊 Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/emotions` | Create new emotion analysis |
| GET | `/emotions` | Get all emotion records |
| GET | `/emotions/{id}` | Get specific emotion record |
| PUT | `/emotions/{id}` | Update emotion record |
| DELETE | `/emotions/{id}` | Delete emotion record |
| POST | `/analyze` | Legacy analysis endpoint |

---

## 🔧 Step-by-Step Thunder Client Testing

### Step 1: Open Thunder Client
1. Open VS Code
2. Click on the Thunder Client icon in the sidebar (⚡)
3. Click "New Request" button

---

### Step 2: Health Check (GET)

**Purpose**: Verify the API is running

1. **Method**: `GET`
2. **URL**: `http://localhost:8000/health`
3. **Headers**: None required
4. **Body**: None
5. **Click Send**

**Expected Response**:
```json
{
  "status": "healthy",
  "total_records": 0,
  "timestamp": "2025-01-XX:XX:XX.XXXXXX"
}
```

---

### Step 3: CREATE Operation (POST)

**Purpose**: Create a new emotion analysis record

1. **Method**: `POST`
2. **URL**: `http://localhost:8000/emotions`
3. **Headers**: 
   - `Content-Type`: `application/json`
4. **Body** (JSON):
   ```json
   {
     "text": "I'm feeling really excited about my new job opportunity!"
   }
   ```
5. **Click Send**

**Expected Response** (Status: 200):
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "text": "I'm feeling really excited about my new job opportunity!",
  "emotion": "Excited",
  "confidence": 0.90,
  "created_at": "2025-01-XX:XX:XX.XXXXXX",
  "updated_at": "2025-01-XX:XX:XX.XXXXXX"
}
```

**📝 Note**: Save the `id` from the response for use in subsequent tests!

---

### Step 4: CREATE More Records

Create 2-3 more records with different texts:

**Record 2**:
```json
{
  "text": "I feel anxious about the upcoming presentation"
}
```

**Record 3**:
```json
{
  "text": "Today was a wonderful day, I'm so happy!"
}
```

---

### Step 5: READ All Records (GET)

**Purpose**: Retrieve all emotion analysis records

1. **Method**: `GET`
2. **URL**: `http://localhost:8000/emotions`
3. **Headers**: None required
4. **Body**: None
5. **Click Send**

**Expected Response** (Status: 200):
```json
[
  {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "text": "I'm feeling really excited about my new job opportunity!",
    "emotion": "Excited",
    "confidence": 0.90,
    "created_at": "2025-01-XX:XX:XX.XXXXXX",
    "updated_at": "2025-01-XX:XX:XX.XXXXXX"
  },
  {
    "id": "987fcdeb-51a2-43d7-b123-987654321000",
    "text": "I feel anxious about the upcoming presentation",
    "emotion": "Anxious",
    "confidence": 0.85,
    "created_at": "2025-01-XX:XX:XX.XXXXXX",
    "updated_at": "2025-01-XX:XX:XX.XXXXXX"
  }
]
```

---

### Step 6: READ Single Record (GET)

**Purpose**: Retrieve a specific emotion record by ID

1. **Method**: `GET`
2. **URL**: `http://localhost:8000/emotions/{RECORD_ID}`
   - Replace `{RECORD_ID}` with an actual ID from previous responses
3. **Headers**: None required
4. **Body**: None
5. **Click Send**

**Expected Response** (Status: 200):
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "text": "I'm feeling really excited about my new job opportunity!",
  "emotion": "Excited",
  "confidence": 0.90,
  "created_at": "2025-01-XX:XX:XX.XXXXXX",
  "updated_at": "2025-01-XX:XX:XX.XXXXXX"
}
```

---

### Step 7: UPDATE Operation (PUT)

**Purpose**: Update an existing emotion record

1. **Method**: `PUT`
2. **URL**: `http://localhost:8000/emotions/{RECORD_ID}`
   - Replace `{RECORD_ID}` with an actual ID
3. **Headers**: 
   - `Content-Type`: `application/json`
4. **Body** (JSON) - Update text:
   ```json
   {
     "text": "I'm feeling incredibly excited and confident about my new role!"
   }
   ```

   **OR** - Update emotion and confidence manually:
   ```json
   {
     "emotion": "Confident",
     "confidence": 0.95
   }
   ```

   **OR** - Update multiple fields:
   ```json
   {
     "text": "I'm feeling much better now after talking to my friend",
     "emotion": "Relieved",
     "confidence": 0.88
   }
   ```

5. **Click Send**

**Expected Response** (Status: 200):
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "text": "I'm feeling incredibly excited and confident about my new role!",
  "emotion": "Happy",
  "confidence": 0.92,
  "created_at": "2025-01-XX:XX:XX.XXXXXX",
  "updated_at": "2025-01-XX:XX:XX.XXXXXX"
}
```

**📝 Note**: The `updated_at` timestamp should be newer than `created_at`

---

### Step 8: DELETE Operation (DELETE)

**Purpose**: Delete an emotion record

1. **Method**: `DELETE`
2. **URL**: `http://localhost:8000/emotions/{RECORD_ID}`
   - Replace `{RECORD_ID}` with an actual ID
3. **Headers**: None required
4. **Body**: None
5. **Click Send**

**Expected Response** (Status: 200):
```json
{
  "message": "Emotion record 123e4567-e89b-12d3-a456-426614174000 deleted successfully"
}
```

---

### Step 9: Verify DELETE Operation

**Purpose**: Confirm the record was deleted

1. **Method**: `GET`
2. **URL**: `http://localhost:8000/emotions/{DELETED_RECORD_ID}`
3. **Click Send**

**Expected Response** (Status: 404):
```json
{
  "detail": "Emotion record not found"
}
```

---

### Step 10: Legacy Endpoint Testing (POST)

**Purpose**: Test backward compatibility

1. **Method**: `POST`
2. **URL**: `http://localhost:8000/analyze`
3. **Headers**: 
   - `Content-Type`: `application/json`
4. **Body** (JSON):
   ```json
   {
     "text": "I'm feeling nervous about tomorrow's interview"
   }
   ```
5. **Click Send**

**Expected Response** (Status: 200):
```json
{
  "emotion": "Anxious",
  "confidence": 0.85
}
```

---

## 🧪 Error Testing Scenarios

### Test 1: Invalid Record ID
- **URL**: `http://localhost:8000/emotions/invalid-id`
- **Method**: `GET`
- **Expected**: 404 Not Found

### Test 2: Empty Request Body
- **URL**: `http://localhost:8000/emotions`
- **Method**: `POST`
- **Body**: `{}`
- **Expected**: 422 Validation Error

### Test 3: Invalid JSON
- **URL**: `http://localhost:8000/emotions`
- **Method**: `POST`
- **Body**: `{ "text": }`
- **Expected**: 400 Bad Request

---

## 📊 Thunder Client Collection Setup

### Creating a Collection
1. In Thunder Client, click "Collections"
2. Click "New Collection"
3. Name it "Emotion Analysis API"
4. Add all the requests above to this collection

### Environment Variables
1. Click "Env" in Thunder Client
2. Create new environment "Local"
3. Add variable:
   - `base_url`: `http://localhost:8000`
4. Use `{{base_url}}` in your requests

---

## 🔍 Response Validation Checklist

For each request, verify:

### CREATE (POST /emotions)
- [ ] Status code is 200
- [ ] Response contains `id`, `text`, `emotion`, `confidence`
- [ ] `created_at` and `updated_at` are present and equal
- [ ] `id` is a valid UUID format

### READ All (GET /emotions)
- [ ] Status code is 200
- [ ] Response is an array
- [ ] Each item has required fields
- [ ] Records are ordered by creation time

### READ Single (GET /emotions/{id})
- [ ] Status code is 200 for valid ID
- [ ] Status code is 404 for invalid ID
- [ ] Response matches the created record

### UPDATE (PUT /emotions/{id})
- [ ] Status code is 200 for valid ID
- [ ] Status code is 404 for invalid ID
- [ ] `updated_at` is newer than `created_at`
- [ ] Only specified fields are updated

### DELETE (DELETE /emotions/{id})
- [ ] Status code is 200 for valid ID
- [ ] Status code is 404 for invalid ID
- [ ] Success message is returned
- [ ] Subsequent GET returns 404

---

## 🚀 Advanced Testing Tips

### 1. **Save Responses as Variables**
In Thunder Client, you can save response values:
- Click on "Tests" tab in request
- Add: `tc.setVar("record_id", tc.response.json.id);`
- Use `{{record_id}}` in subsequent requests

### 2. **Automated Testing Scripts**
Add test scripts to verify responses:
```javascript
// Verify status code
tc.test("Status code is 200", () => {
    tc.expect(tc.response.status).to.equal(200);
});

// Verify response structure
tc.test("Response has required fields", () => {
    const json = tc.response.json;
    tc.expect(json).to.have.property('id');
    tc.expect(json).to.have.property('emotion');
    tc.expect(json).to.have.property('confidence');
});
```

### 3. **Performance Testing**
- Monitor response times in Thunder Client
- Test with larger datasets
- Check concurrent requests

---

## 📈 Sample Test Data

Use these text samples for varied emotion analysis:

```json
// Happy emotions
{"text": "I just got promoted at work! I'm so thrilled and grateful!"}
{"text": "My family surprised me with a birthday party, I'm overjoyed!"}

// Sad emotions  
{"text": "I'm feeling down after hearing the disappointing news"}
{"text": "It's been a tough week and I'm struggling to stay positive"}

// Anxious emotions
{"text": "I have a big presentation tomorrow and I'm really nervous"}
{"text": "The uncertainty about the future is making me feel anxious"}

// Excited emotions
{"text": "I can't wait for my vacation next week, I'm so excited!"}
{"text": "Starting my new hobby has me feeling energized and excited"}

// Angry emotions
{"text": "I'm frustrated with the constant delays in this project"}
{"text": "The unfair treatment at work is making me really angry"}
```

---

## 🎯 Success Criteria

Your CRUD testing is complete when you can:

1. ✅ **Create** multiple emotion records successfully
2. ✅ **Read** all records and individual records by ID
3. ✅ **Update** existing records with new data
4. ✅ **Delete** records and verify they're gone
5. ✅ Handle error cases (404, validation errors)
6. ✅ Verify data persistence across operations
7. ✅ Test the legacy `/analyze` endpoint

---

## 🔧 Troubleshooting

### Common Issues:

1. **Connection Refused**
   - Ensure FastAPI server is running
   - Check if port 8000 is available
   - Verify URL format

2. **404 Not Found**
   - Check endpoint spelling
   - Verify record ID exists
   - Ensure server is running

3. **422 Validation Error**
   - Check JSON format
   - Verify required fields are present
   - Check data types match schema

4. **CORS Issues**
   - Server includes CORS middleware
   - Should work from Thunder Client
   - Check browser console if testing from web

---

This comprehensive guide covers all aspects of CRUD testing using Thunder Client. Follow each step systematically to ensure your API works correctly!