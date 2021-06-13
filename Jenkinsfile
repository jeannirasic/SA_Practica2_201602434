node {
	stage('SCM') {
		git branch: 'master', url: 'https://github.com/jeannirasic/SA_Practica2_201602434.git'
	}

	stage('Build test') {
		sh '''
			cd Front/
			npm install
			npm run test --watch=false
			npm run build --prod
		'''
	}
	
}
