from django.db import models

class Compiler(models.Model):
    shortname = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    compile_cmd = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CompilerConfiguration(models.Model):
    compiler = models.ForeignKey(Compiler, on_delete=models.CASCADE)
    shortname = models.CharField(max_length=50)
    flags = models.CharField(max_length=100)

    def __str__(self):
        return self.compiler.name + " " + self.flags

class Assembly(models.Model):
    hash = models.CharField(max_length=64, primary_key=True)
    data = models.TextField()

    def __str__(self):
        return self.data

class Compilation(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    compiler_config = models.ForeignKey(CompilerConfiguration, on_delete=models.CASCADE)
    source_code = models.TextField()
    assembly = models.ForeignKey(Assembly, on_delete=models.CASCADE)

class Scratch(models.Model):
    slug = models.SlugField(primary_key=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    compiler_config = models.ForeignKey(CompilerConfiguration, on_delete=models.CASCADE)
    target_asm = models.ForeignKey(Assembly, on_delete=models.CASCADE)
    source_code = models.TextField()
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    owner = models.UUIDField(null=True, blank=True)

    def __str__(self):
        return self.slug
