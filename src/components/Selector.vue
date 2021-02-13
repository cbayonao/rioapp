<template>
  <div class="container mt-3 mb-3">
    <!-- Cambiar por componentes -->
    <div class="row mb-5">
      <router-link
        type="button"
        class="btn btn-lg btn-primary rounded-pill pt-5 pb-5"
        to="/bdua"
      >
        <img src="../assets/Logo-adres.png" alt="adres" />
        {{ bduaName }}
      </router-link>
    </div>
    <br />
    <div class="row mb-5">
      <router-link
        type="button"
        class="btn btn-lg btn-secondary rounded-pill pt-5 pb-5"
        to="/sisben"
      >
        <img src="../assets/sisben_logo.png" alt="sisben" />
        {{ sisbenName }}
      </router-link>
    </div>
    <br />
    <div class="row mb-5">
      <router-link
        type="button"
        class="btn btn-lg btn-success rounded-pill pt-5 pb-5"
        to="/entintrionegro"
      >
        <img src="../assets/logo-rionegro.png" alt="rionegro" />
        {{ entIntName }}
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  setup() {
    const bduaName = "BDUA MinSalud";
    const sisbenName = "Sisben";
    const entIntName = "Entidades Integradas";
    return {
      bduaName,
      sisbenName,
      entIntName,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style></style>
