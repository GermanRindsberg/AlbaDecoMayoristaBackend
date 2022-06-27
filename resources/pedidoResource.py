from datetime import date
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity
from models.maestroDetalle import MaestroDetalle
from models.pedido import Pedido
from schemas.pedidoSchema import pedidosSchema, pedidoSchema
from resources.emailService import enviarEmailPedidoRecibido, enviarEmailPedidoEnviado, enviarEmailPedidoSeñado

class PedidoListResource(Resource):
 
    def get(self):
        pedidos = Pedido.get_all()
        return pedidosSchema.dump(pedidos)
  
    @jwt_required()
    def post(self):
        form_data: dict = request.get_json()
        nombreUsuario=form_data['nombreUsuario']
        emailUsuario=form_data['emailUsuario']
        pedido = Pedido()
        pedido.fechaPedido=date.today()
        if form_data['montoTotal']:
            pedido.montoTotal=form_data['montoTotal']
        if form_data['subTotal']:
            pedido.subTotal=form_data['subTotal']
        if form_data['descuento']:
            pedido.descuento=form_data['descuento']
        else:
            pedido.descuento=0.0
        pedido.idUsuario=get_jwt_identity()
        pedido.estado='recibido'
        pedido.save(is_new=True)

        #maestroDetalle
        if form_data['productos']:
            listaProductos= form_data['productos']
            for producto in listaProductos:
                maestroDetalle=MaestroDetalle()
                maestroDetalle.idPedido=pedido.id
                cantidad=producto['cantidad']
                precio=producto['producto']['precio']

                maestroDetalle.idVariante=producto['variante']['id']
                maestroDetalle.idProducto=producto['variante']['idProducto']
                maestroDetalle.precioUnitario=precio
                maestroDetalle.cantidad= cantidad
                maestroDetalle.subTotal= int(cantidad) * precio
                maestroDetalle.save(is_new=True)
        
        listaProductoMail=[]
        descuento=0
        for p in listaProductos:
            listaProductoMail.append([p["producto"]['nombre'],p["variante"]['color'],int(p['cantidad']),float(p['producto']['precio'])])

        enviarEmailPedidoRecibido(emailUsuario,nombreUsuario, listaProductoMail,form_data['montoTotal'],descuento, form_data['montoTotal']-descuento)

        return pedidoSchema.dump(pedido), 201


class PedidoResource(Resource):

    def get(self, idPedido):
        pedido = Pedido.get_by_id(idPedido)
        return pedidoSchema.dump(pedido)
    
    @jwt_required()
    def patch(self, idPedido):
        form_data: dict = request.get_json()
        pedido = Pedido.get_by_id(idPedido)
        if form_data['estado']=='señado':
            pedido.fechaSeña= date.today()
            pedido.estado='señado'
            enviarEmailPedidoSeñado(pedido.usuario.email, pedido.usuario.perfil.nombre, pedido.id)
        elif form_data['estado']=='listo':
            pedido.estado='listo'
        elif form_data['estado']=='archivado':
            pedido.estado='archivado'
        elif form_data['estado']=='recibido':
            pedido.estado='recibido'
        else:
            pedido.fechaEnvio=date.today()
            pedido.numeroGuia=form_data['numeroGuia']
            pedido.transporte=form_data['transporte']
            enviarEmailPedidoEnviado(pedido.usuario.email, pedido.usuario.perfil.nombre, pedido.id, pedido.transporte, pedido.numeroGuia)
            pedido.estado='enviado'

        pedido.save(is_new=False)

        return 'editado'
  
class PedidoPorUser(Resource):
    
    def get(self, idUsuario):
        pedido = Pedido.getPorIdUsuario(idUsuario)
        return pedidosSchema.dump(pedido)

