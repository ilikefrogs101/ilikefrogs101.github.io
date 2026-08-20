fetch("/navbar.html")
.then(r => r.ok ? r.text() : Promise.reject())
.then(html => {
	navbar.innerHTML = html;

	document.querySelectorAll("#navbar a").forEach(a => {
		if (new URL(a.href).pathname === location.pathname) {
			a.className = "current-navbar-link";
		}
	});
}).catch(console.error);