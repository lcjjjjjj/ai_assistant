<script setup>
import Manu from '../components/Manu.vue'
</script>

<template>
    <div class="common-layout">
      <el-container>
        <Manu />
        <el-container>
          <el-header>Header</el-header>
          <el-main><RouterView /></el-main>
        </el-container>
      </el-container>
    </div>
</template>

<style scopd>

.common-layout {
  height: 100%;
}

.el-container {
    height: 100%;
}

</style>