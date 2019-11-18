package myBot;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

import ai.abstraction.AbstractAction;
import ai.abstraction.AbstractionLayerAI;
import ai.abstraction.Harvest;
import ai.abstraction.pathfinding.AStarPathFinding;
import ai.abstraction.pathfinding.PathFinding;
import ai.core.AI;
import ai.core.ParameterSpecification;
import rts.GameState;
import rts.PartiallyObservableGameState;
import rts.PhysicalGameState;
import rts.Player;
import rts.PlayerAction;
import rts.UnitAction;
import rts.units.Unit;
import rts.units.UnitType;
import rts.units.UnitTypeTable;

public class Version2 extends AbstractionLayerAI{
	UnitTypeTable utt = null;
	UnitType workerType;
	UnitType baseType;
	UnitType barracksType;
	UnitType lightType;
	UnitType heavyType;
	UnitType rangedType;
	//the counter
	int counter=0;
	boolean resourse = true;
	int rushflag=0;
	int base_init_distance=0;
	
	// This is the default constructor that microRTS will call:
	public Version2(UnitTypeTable a_utt) {
	        this(a_utt, new AStarPathFinding());
	    }
	public Version2(UnitTypeTable a_utt, PathFinding a_pf) {
		
        super(a_pf);
       // System.out.print("start");
        
        reset(a_utt);
    }	
	public void reset() {
    	super.reset();
    }



    // This will be called by microRTS when it wants to create new instances of this bot (e.g., to play multiple games).
    public AI clone() {
        return new Version2(utt, pf);
    }
    

    public void reset(UnitTypeTable a_utt)  
    {
    	
        utt = a_utt;
        if (utt!=null) {
            workerType = utt.getUnitType("Worker");
            baseType = utt.getUnitType("Base");
            barracksType = utt.getUnitType("Barracks");
            lightType = utt.getUnitType("Light");
            rangedType=utt.getUnitType("Ranged");
            heavyType = utt.getUnitType("Heavy");
        }
        
    }   
       
    // Called by microRTS at each game cycle.
    // Returns the action the bot wants to execute.
    public PlayerAction getAction(int player, GameState gs) {
    	
    	
    	 PhysicalGameState pgs = gs.getPhysicalGameState();
         Player p = gs.getPlayer(player);
         PlayerAction pa = new PlayerAction();
         //get the init base distance
         if (counter==0){
        	 get_init_basedistance(player,pgs);      	 
        	 counter+=1;
         }
         
         // behavior of bases:
         for(Unit u:pgs.getUnits()) {
             if (u.getType()==baseType && 
                 u.getPlayer() == player && 
                 gs.getActionAssignment(u)==null) {
            	 if (base_init_distance>22)
            		 {baseBehavior(u,p,pgs);}
            	 else{rushbaseBehavior(u,p,pgs);}
                }
         }
        
         // behavior of melee units:
         for(Unit u:pgs.getUnits()) {

             if (u.getType().canAttack && !u.getType().canHarvest && 
                 u.getPlayer() == player && 
                 gs.getActionAssignment(u)==null) {           	                       	 		
           
            	//defenceUnitBehavior(u,p,gs);
            	 
                meleeUnitBehavior(u,p,gs);
            	
             }        
         }
         //behavior of barracks
         for(Unit u:pgs.getUnits()) {
             if (u.getType()==barracksType && 
                 u.getPlayer() == player && 
                 gs.getActionAssignment(u)==null) {
                 barracksBehavior(u,p,gs);
             }        
         }

         // behavior of workers:
         List<Unit> workers = new LinkedList<Unit>();
         for(Unit u:pgs.getUnits()) {
             if (u.getType().canHarvest && 
                 u.getPlayer() == player) {
                 workers.add(u);
             }        
         }
         if(base_init_distance>22){workersBehavior(workers,p,gs);}
         else{rushworkersBehavior(workers,p,gs);}
         
         
                 
         return translateActions(player,gs);
    }
    public void get_init_basedistance(int Player,PhysicalGameState pgs){
    	Unit mbase=null;
    	Unit hbase=null;

    	for(Unit u:pgs.getUnits()) {
            if (u.getType()==baseType ) {
            	if(u.getPlayer()==Player)
            		mbase=u;
                  
            	else{
            		hbase=u;
            	}
            }
        }  
    	base_init_distance=Math.abs(mbase.getX() - hbase.getX()) + Math.abs(mbase.getY() - hbase.getY());
    
    }
    private void barracksBehavior(Unit u, Player p, GameState gs) {
		// TODO Auto-generated method stub
    	int Rangednums=0;
    	int lightnums=0;
    	int basenums=0;
    	PhysicalGameState pgs = gs.getPhysicalGameState();
    	
    	for(Unit unums:pgs.getUnits()) {
            if (unums.getType()==rangedType && 
                unums.getPlayer() == p.getID()) {
                Rangednums+=1;
            } 
            if (unums.getType()==lightType && 
                unums.getPlayer() == p.getID()) {
                lightnums+=1;
            }
            if(unums.getType()==baseType && 
                unums.getPlayer() == p.getID()){
            	basenums++;
            	
            }
        }
    	if (basenums==0&&p.getResources()<=rangedType.cost+baseType.cost){
    		
    		
    	}
    	else{
    	//System.out.println(Rangednums+" "+lightnums);
    		if (p.getResources() >= lightType.cost&&(Rangednums>=(lightnums+Rangednums)*2/3||lightnums<=2)) {
    			train(u, lightType);
    		}
    		else if (p.getResources() >= rangedType.cost&&lightnums>=(Rangednums+lightnums)/3){
    			train(u, rangedType);
    		}
    	}
     	
        }
        
	
	public void workersBehavior(List<Unit> workers,Player p, GameState gs){
        PhysicalGameState pgs = gs.getPhysicalGameState();
        int nbases = 0;
        int nbarracks = 0;
        int n=0;
        int resourcesUsed = 0;
        List<Unit> freeWorkers = new LinkedList<Unit>();
      
        freeWorkers.addAll(workers);
        

        if (workers.isEmpty()) {
            return;
        }

        for (Unit u2 : pgs.getUnits()) {
            if (u2.getType() == baseType
                    && u2.getPlayer() == p.getID()) {
                nbases++;
            }
            if (u2.getType() == barracksType
                    && u2.getPlayer() == p.getID()) {
                nbarracks++;
            }
        }

        List<Integer> reservedPositions = new LinkedList<Integer>();
        if (nbases == 0 && !freeWorkers.isEmpty()) {
            // build a base:
            if (p.getResources() >= baseType.cost + resourcesUsed) {
                Unit u = freeWorkers.remove(0);
                buildIfNotAlreadyBuilding(u,baseType,u.getX(),u.getY(),reservedPositions,p,pgs);
                resourcesUsed += baseType.cost;
            }
        }

        if (nbarracks == 0) {
            // build a barracks:
            if (p.getResources() >= barracksType.cost + resourcesUsed && !freeWorkers.isEmpty()) {
                Unit u = freeWorkers.remove(0);
                buildIfNotAlreadyBuilding(u,barracksType,u.getX(),u.getY(),reservedPositions,p,pgs);
                resourcesUsed += barracksType.cost;
            }
        }
        
        	
        


        // harvest with all the free workers:
        for (Unit u : freeWorkers) {
            Unit closestBase = null;
            Unit closestResource = null;
            int closestDistance = 0;
            for (Unit u2 : pgs.getUnits()) {
                if (u2.getType().isResource) {
                    int d = Math.abs(u2.getX() - u.getX()) + Math.abs(u2.getY() - u.getY());
                    if (closestResource == null || d < closestDistance) {
                        closestResource = u2;
                        closestDistance = d;
                    }
                }
            }
            closestDistance = 0;
            for (Unit u2 : pgs.getUnits()) {
                if (u2.getType().isStockpile && u2.getPlayer()==p.getID()) {
                    int d = Math.abs(u2.getX() - u.getX()) + Math.abs(u2.getY() - u.getY());
                    if (closestBase == null || d < closestDistance) {
                        closestBase = u2;
                        closestDistance = d;
                    }
                }
            }
            if (closestResource != null && closestBase != null) {
                AbstractAction aa = getAbstractAction(u);
                if (aa instanceof Harvest) {
                    Harvest h_aa = (Harvest)aa;
                    if (h_aa.getTarget() != closestResource || h_aa.getBase()!=closestBase) harvest(u, closestResource, closestBase);
                } else {
                    harvest(u, closestResource, closestBase);
                }
            }
        }
        
    }
    public void meleeUnitBehavior(Unit u,Player p, GameState gs){
    	PhysicalGameState pgs = gs.getPhysicalGameState();
        Unit closestResource = null;
        Unit mbase=null;
        Unit mbarrack=null;
        int RclosestDistance = 0;
        for (Unit ru:pgs.getUnits()){
        	if(ru.getType()==baseType&&ru.getPlayer()==p.getID()){
        		mbase=ru;
        	}
        	if(ru.getType()==barracksType&&ru.getPlayer()==p.getID()){
        		mbarrack=ru;
        	}
        }
        if(mbase!=null){
        for (Unit ru : pgs.getUnits()) {
            if (ru.getType().isResource) {
                int d = Math.abs(ru.getX() - mbase.getX()) + Math.abs(ru.getY() - mbase.getY());
                if (closestResource == null || d < RclosestDistance) {
                	closestResource = ru;
                    RclosestDistance = d;
                    
                	}
               }
            }}
        if ((RclosestDistance>12||closestResource==null)/*&&(mbarrack==null||gs.getActionAssignment(mbarrack).action.getType()==UnitAction.TYPE_PRODUCE)*/)
        	{rushflag=1;}
        if(rushflag==0){defenceUnitBehavior(u,p,gs);}
        else{meleeUnitAttack(u,p,gs);
        }
    }
    public void meleeUnitAttack(Unit u,Player p, GameState gs){       
    	PhysicalGameState pgs = gs.getPhysicalGameState();    	
        Unit closestEnemy = null;
        int closestDistance = 0;
        for (Unit u2 : pgs.getUnits()) {
            if (u2.getPlayer() >= 0 && u2.getPlayer() != p.getID()) {
                int d = Math.abs(u2.getX() - u.getX()) + Math.abs(u2.getY() - u.getY());
                if (closestEnemy == null || d < closestDistance) {
                    closestEnemy = u2;
                    closestDistance = d;
                }
            }
        }
        if (closestEnemy != null) {
            attack(u, closestEnemy);
        } else if (gs instanceof PartiallyObservableGameState) {
            PartiallyObservableGameState pogs = (PartiallyObservableGameState)gs;
         
            int closest_x = 0;
            int closest_y = 0;
            closestDistance = -1;
            for(int i = 0;i<pgs.getHeight();i++) {
                for(int j = 0;j<pgs.getWidth();j++) {
                    if (!pogs.observable(j, i)) {
                        int d = (u.getX() - j)*(u.getX() - j) + (u.getY() - i)*(u.getY() - i);
                        if (closestDistance == -1 || d<closestDistance) {
                            closest_x = j;
                            closest_y = i;
                            closestDistance = d;
                        }
                    }
                }
            }
            if (closestDistance!=-1) {
                move(u, closest_x, closest_y);
            }
        }
    }
    //The defence unit behavior
    public void defenceUnitBehavior(Unit u,Player p, GameState gs){
    	PhysicalGameState pgs = gs.getPhysicalGameState();
        Unit closestEnemy = null;
        int defenceDistance=0;
        int closestDistance = 0;
        int attackarea=4;
        int mybase = 0;
        Unit mbase=null;
        for(Unit u2:pgs.getUnits()) {
            if (u2.getPlayer()>=0 && u2.getPlayer()!=p.getID()) { 
                int d = Math.abs(u2.getX() - u.getX()) + Math.abs(u2.getY() - u.getY());
                if (closestEnemy==null || d<closestDistance) {
                    closestEnemy = u2;
                    closestDistance = d;
                }
            }
            else if(u2.getPlayer()==p.getID() && u2.getType() == baseType)
            {
            	mbase=u2;
                mybase = Math.abs(u2.getX() - u.getX()) + Math.abs(u2.getY() - u.getY());
            }
        }
        
        if (u.getType()==lightType){
        	defenceDistance=5;
        	attackarea=5;
        	
        }
        /*else if (u.getType()==heavyType){
        	defenceDistance=10;
        	
        }*/
        else{
        	defenceDistance=4;
        	attackarea=8;
        }

        if ((closestDistance < attackarea || mybase < defenceDistance)) {
        	
        
        	attack(u,closestEnemy);
        }
        else if(mybase > defenceDistance+1)
        {
        	
        	attack(u,mbase);
            
        }
        else{
        	attack(u,null);
        }
    }

    public void baseBehavior(Unit u,Player p, PhysicalGameState pgs){
    	int nums=0;
    	for(Unit worker:pgs.getUnits()){
    		if (worker.getType().canHarvest&&worker.getPlayer()==p.getID()){
    			nums=nums+1;
    			
    		}  		
    	}
   
    	if (p.getResources()>=workerType.cost&&nums<=2 ) train(u, workerType);
    }
    public void rushbaseBehavior(Unit u,Player p, PhysicalGameState pgs) {
        if (p.getResources()>=workerType.cost) train(u, workerType);
    }
    
    public void rushworkersBehavior(List<Unit> workers,Player p, GameState gs) {
        PhysicalGameState pgs = gs.getPhysicalGameState();
        int nbases = 0;
        int resourcesUsed = 0;
        Unit harvestWorker = null;
        List<Unit> freeWorkers = new LinkedList<Unit>();
        freeWorkers.addAll(workers);
        
        if (workers.isEmpty()) return;
        
        for(Unit u2:pgs.getUnits()) {
            if (u2.getType() == baseType && 
                u2.getPlayer() == p.getID()) nbases++;
        }
        
        List<Integer> reservedPositions = new LinkedList<Integer>();
        if (nbases==0 && !freeWorkers.isEmpty()) {
            // build a base:
            if (p.getResources()>=baseType.cost + resourcesUsed) {
                Unit u = freeWorkers.remove(0);
                buildIfNotAlreadyBuilding(u,baseType,u.getX(),u.getY(),reservedPositions,p,pgs);
                resourcesUsed+=baseType.cost;
            }
        }
        
        if (freeWorkers.size()>0) harvestWorker = freeWorkers.remove(0);
        
        // harvest with the harvest worker:
        if (harvestWorker!=null) {
            Unit closestBase = null;
            Unit closestResource = null;
            int closestDistance = 0;
            for(Unit u2:pgs.getUnits()) {
                if (u2.getType().isResource) { 
                    int d = Math.abs(u2.getX() - harvestWorker.getX()) + Math.abs(u2.getY() - harvestWorker.getY());
                    if (closestResource==null || d<closestDistance) {
                        closestResource = u2;
                        closestDistance = d;
                    }
                }
            }
            closestDistance = 0;
            for(Unit u2:pgs.getUnits()) {
                if (u2.getType().isStockpile && u2.getPlayer()==p.getID()) { 
                    int d = Math.abs(u2.getX() - harvestWorker.getX()) + Math.abs(u2.getY() - harvestWorker.getY());
                    if (closestBase==null || d<closestDistance) {
                        closestBase = u2;
                        closestDistance = d;
                    }
                }
            }
            if (closestResource!=null && closestBase!=null) {
                AbstractAction aa = getAbstractAction(harvestWorker);
                if (aa instanceof Harvest) {
                    Harvest h_aa = (Harvest)aa;
                    if (h_aa.getTarget() != closestResource || h_aa.getBase()!=closestBase) harvest(harvestWorker, closestResource, closestBase);
                } else {
                    harvest(harvestWorker, closestResource, closestBase);
                }
            }
        }
        
        for(Unit u:freeWorkers) meleeUnitAttack(u, p, gs);
        
    }
    // This will be called by the microRTS GUI to get the
    // list of parameters that this bot wants exposed
    // in the GUI.
    public List<ParameterSpecification> getParameters()
    {
    	List<ParameterSpecification> parameters = new ArrayList<>();
    	parameters.add(new ParameterSpecification("PathFinding", PathFinding.class, new AStarPathFinding()));
        return parameters;
    }
}

	
	    



