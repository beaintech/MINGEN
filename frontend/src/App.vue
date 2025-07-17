<template>
  <div class="container">
    <h1>MINGEN - StarSeed - 命运生成器</h1>

    <form @submit.prevent="submitForm">
      <label for="name">姓名:</label>
      <input type="text" id="name" v-model="formData.name" required />

      <label for="birthday">出生日期和时间:</label>
      <input type="datetime-local" id="birthday" v-model="formData.birthday" required />

      <label for="birthplace">出生地:</label>
      <input type="text" id="birthplace" v-model="formData.birthplace" required />

      <label for="gender">性别:</label>
      <select id="gender" v-model="formData.gender">
          <option value="男">男</option>
          <option value="女">女</option>
          <option value="未提供">未提供</option>
      </select>

      <button type="submit">提交</button>
    </form>

    <div v-if="response">
      <h2>结果:</h2>
      <div v-html="renderedContent"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import { marked } from 'marked'

const formData = ref({
  name: '',
  birthday: '',
  birthplace: '',
  gender: ''
})

const response = ref(null)

// GPT 返回的 result
const renderedContent = computed(() => {
  if (typeof response.value.result === 'string') {
    return marked(response.value.result)
  }
  return '<p>暂无内容</p>'
})

const submitForm = async () => {
  try {
    // const res = await axios.post('http://127.0.0.1:8000/submit', formData.value)
    const res = await axios.post('https://starseed-api.onrender.com/submit', formData.value)
    response.value = res.data
  } catch (err) {
    console.error('Error submitting:', err)
    response.value = { error: '提交失败，请检查服务端是否运行' }
  }
}
</script>

<style scoped>
.container {
  max-width: 75%;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 12px;
  font-family: Arial, sans-serif;
}
input, button {
  display: block;
  width: 100%;
  margin-bottom: 15px;
  padding: 8px;
  font-size: 16px;
}
button {
  background-color: #409eff;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
button:hover {
  background-color: #66b1ff;
}

.markdown-table table {
  width: 100%;
  table-layout: fixed;
}

.markdown-table td:first-child {
  width: 25%;
  font-weight: bold;
}

</style>
