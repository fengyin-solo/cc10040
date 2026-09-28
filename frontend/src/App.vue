<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">城市燃气管道巡检平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向燃气管道巡线、调压站运行、泄漏检测处置、第三方施工监护与停气复气作业的一体化管网运维后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "燃气管道", path: "/pipeline" }, { label: "调压站", path: "/regulator" }, { label: "阀门井", path: "/valve" }, { label: "阴极保护", path: "/cathode" }, { label: "泄漏检测", path: "/leak" }, { label: "巡检路线", path: "/route" }, { label: "抢修作业", path: "/rush" }, { label: "燃气表", path: "/meter" }, { label: "入户安检", path: "/safetycheck" }, { label: "管龄评估", path: "/pipeage" }, { label: "第三方施工监护", path: "/thirdparty" }, { label: "停气复气", path: "/shutoff" }, { label: "隐患整改", path: "/hazard" }, { label: "抢修队伍", path: "/team" }, { label: "燃气具", path: "/appliance" }, { label: "压力监测", path: "/pressure" }, { label: "用户开户", path: "/account" }, { label: "应急演练", path: "/emergency" }]
</script>
